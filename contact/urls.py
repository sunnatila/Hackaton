from django.urls import path
from .views import ContactCreateApiView

urlpatterns = [
    path('contact/create', ContactCreateApiView.as_view())
]

