from django import forms
from django.forms import TextInput, Textarea, FileInput, FileField
from django.contrib.auth.forms import AuthenticationForm

from models import table_post_description

class Document(forms.ModelForm):
    class Meta :
        model = table_post_description
        fields = ['judul', 'deskripsi', 'document']
        widgets = {
            'judul' : TextInput(attrs={'class' : 'form-control', 'placeholder':'Masukkan Judul'}),
            'deskripsi' : Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan Deskripsi'}),
        }
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan Username'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Username'}))