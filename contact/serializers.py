
from rest_framework import serializers
from .models import Contact, Group

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('status',)


    def validate(self, data):
        phone = data.get('phone', '')
        if not phone:
            raise serializers.ValidationError({"status": "Telefon raqami kiritilishi shart."})

        if phone.startswith('+998'):
            formatted_phone = phone
        elif phone.isdigit():
            formatted_phone = '+998' + phone.lstrip('0')
        else:
            raise serializers.ValidationError("Telefon raqami noto'g'ri formatda.")

        data['phone'] = formatted_phone

        # Validate dev_type
        valid_dev_types = [choice[0] for choice in Contact.DEVELOPER_TYPE]
        if data.get('dev_type') not in valid_dev_types:
            raise serializers.ValidationError(f"Yaroqsiz dev_type. Yaroqli turlar: {', '.join(valid_dev_types)}")

        return data

    def create(self, validated_data):
        phone = validated_data.get('phone')
        dev_type = validated_data.get('dev_type')

        # Check if a contact with this phone number already exists
        existing_contact = Contact.objects.filter(phone=phone).first()
        if existing_contact:
            existing_contact.status = "Bu telefon raqamli foydalanuvchi mavjud"
            existing_contact.save()
            raise serializers.ValidationError({
                'status': "Bu telefon raqamli foydalanuvchi mavjud"
            })

        # Create new contact
        contact = Contact.objects.create(**validated_data)

        # Check group availability and assign contact
        group = self.check_group_availability(contact)
        if group is None:
            raise serializers.ValidationError({
                'status': "Barcha joylar o'zlashtirilgan, bo'sh joy mavjud emas."
            })

        self.assign_to_group(contact, group)
        return contact

    def check_group_availability(self, contact):
        if contact.dev_type == 'Frontend':
            group = Group.objects.filter(frontend_dev=None).first() or Group.objects.filter(frontend_dev2=None).first()
        elif contact.dev_type == 'Backend':
            group = Group.objects.filter(backend_dev=None).first()
        elif contact.dev_type == 'Designer':
            group = Group.objects.filter(designer=None).first()
        else:
            group = None

        # If no group is available and there are less than 6 groups, create a new group
        if not group:
            if Group.objects.count() < 6:
                group = Group.objects.create(
                    backend_dev=None,
                    frontend_dev=None,
                    frontend_dev2=None,
                    designer=None
                )
            else:
                group = None

        return group

    def assign_to_group(self, contact, group):
        if contact.dev_type == 'Frontend':
            if group.frontend_dev is None:
                group.frontend_dev = contact
            else:
                group.frontend_dev2 = contact
        elif contact.dev_type == 'Backend':
            group.backend_dev = contact
        elif contact.dev_type == 'Designer':
            group.designer = contact

        group.save()
        contact.status = "Siz hackaton ga muvaffaqiyatli qo'shildingiz"
        contact.save()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def validate(self, data):
        # Guruh yaratishda faqat 6 ta guruh bo'lishi kerak
        if not self.instance and Group.objects.count() >= 6:
            raise serializers.ValidationError("Faqat 6 ta guruh yaratilishi mumkin.")
        else:
            return data

    def create(self, validated_data):
        group = Group(**validated_data)
        group.save()
        return group
