from rest_framework import serializers
from .models import Contact, Group


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('status',)

    def validate_dev_type(self, value):
        valid_dev_types = dict(Contact.DEVELOPER_TYPE).keys()
        if value not in valid_dev_types:
            raise serializers.ValidationError(f"Invalid dev_type. Valid options are: {', '.join(valid_dev_types)}")
        return value

    def create(self, validated_data):
        # Check if there's a spot available in any group
        contact = Contact(**validated_data)
        group = self.check_group_availability(contact)

        # If no group is available, return error message without saving the contact
        if group is None:
            raise serializers.ValidationError(detail={
                'status': 'Barcha joylar o\'zlashtirilgan, bo\'sh joy mavjud emas.'
            })

        # Save the contact if a spot is available
        contact.save()

        # Assign the contact to the appropriate group
        self.assign_to_group(contact, group)

        return contact

    def check_group_availability(self, contact):
        group = None
        if contact.dev_type == 'Frontend':
            group = Group.objects.filter(frontend_dev=None).first() or Group.objects.filter(frontend_dev2=None).first()
        elif contact.dev_type == 'Backend':
            group = Group.objects.filter(backend_dev=None).first()
        elif contact.dev_type == 'Designer':
            group = Group.objects.filter(designer=None).first()

        # If no available group is found and there are already 6 groups, create a new group
        if not group:
            if Group.objects.count() < 6:
                group = Group.objects.create(
                    backend_dev=None,
                    frontend_dev=None,
                    frontend_dev2=None,
                    designer=None
                )
            else:
                return None

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

        # Save the updated group
        group.save()

        # Set status to success
        contact.status = "Siz hackaton ga muvaffaqiyatli qoshildingiz"
        contact.save()
