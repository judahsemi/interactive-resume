from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

# from django.contrib.auth.models import User



# Create your forms here.
class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def save(self, commit=True):
        return None


class ConfirmDeleteForm(forms.Form):
    def save(self, obj, commit=True):
        if commit:
            obj.delete()
        return obj


class BlankForm(forms.Form):
    pass

