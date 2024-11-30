from django import forms
from .models import CustomUserModel,Product

class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUserModel
        fields=['username','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
        }


class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})) 
    remember_me=forms.BooleanField(required=False,widget=forms.CheckboxInput()) 


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','description','image']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Product Name'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),

        }

class OrderForm(forms.Form):
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}))
    address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    