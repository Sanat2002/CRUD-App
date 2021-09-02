from django import forms
from django.forms import widgets
from .models import users

class employee(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            # render_value means that it will show the password when we update the object
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control'})     
        }