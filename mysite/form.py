from django import forms

class UserRegisterForm(forms.Form):
    user_id = forms.CharField(label='您的帳號', max_length=50)
    user_pass = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)
    user_password_confirm = forms.CharField(label='輸入確認密碼', widget=forms.PasswordInput)
    
class LoginForm(forms.Form):
    user_id = forms.CharField(label='您的帳號', max_length=50, initial='')
    user_pass = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)   

class Form(forms.Form):
    _query = forms.CharField(label='搜尋')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    publication_date = forms.DateField()

    def __str__(self):
        return self.title