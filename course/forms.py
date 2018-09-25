from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label=r'学生姓名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class_id = forms.ChoiceField(
        choices=(('dq1', '电气1班'), ('dq2', '电气2班'), ('dx1', '电信1班'), ('dx2', '电信2班')),
        label=r'班级',
    )
    phone_number = forms.CharField(max_length=11, label=r'手机号码', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=30, label='邮箱', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    school_id = forms.CharField(max_length=10, label=r'学号', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=256, label=r'密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=256, label=r'密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')
