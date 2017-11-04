from django.forms import forms

from landing.models import Users


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = [""]