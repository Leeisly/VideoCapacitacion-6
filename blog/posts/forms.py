from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Usuario = get_user_model()



# class UserAdminCreationForm(forms.ModelForm):
   
#     password1 = forms.CharField(label='password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = Usuario
#         fields = ['email']

#     def clean(self):
       
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password2 = cleaned_data.get("password2")
#         if password is not None and password != password2:
#             self.add_error("password2", "Your passwords must match")
#         return cleaned_data

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         usuario = super().save(commit=False)
#         usuario.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return usuario


# # class GuestForm(forms.Form):
# #     email = forms.EmailField(label='Email')

# # class LoginForm(forms.Form):
# #     email = forms.EmailField(label="Email")
# #     password = forms.CharField(widget=forms.PasswordInput)





# class RegisterForm(forms.ModelForm):
#     # username = forms.CharField()
#     # email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

#     class Meta:
#         model = Usuario
#         fields = ['username']


#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = Usuario.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("username is taken")
#         return username
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password2 = cleaned_data.get("password2")
#         if password is not None and password != password2:
#             self.add_error("password2", "Your passwords must match")
#         return cleaned_data



# class UserAdminChangeForm(forms.ModelForm):
    
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Usuario
#         fields = ['email', 'password', 'is_active', 'admin']

#     def clean_password(self):
        
#         return self.initial["password"]