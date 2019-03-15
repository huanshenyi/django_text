from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message='二回の入力一致しません')
        return cleaned_data


    class Meta:
        model = User
        fields = "__all__"


class SigninForm(forms.ModelForm):

    def get_error(self):
        news_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.values():
            for message_dicts in messages:
                for key, message in message_dicts.items():
                    if key == 'message':
                         news_errors.append(message)
        return news_errors


    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username': {
                'min_length': 'ユーザーネーム4桁以上'
            },
            'password': {
                'min_length': 'パスワードは4桁以上'
            }

        }


