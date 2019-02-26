from django import forms
from django.core import validators
from .models import User

class MyForm(forms.Form):
    #email = forms.EmailField(error_messages={'invalid': '正しいメールを入力してください'})
    #price = forms.FloatField(error_messages={'invalid': '小数点含む数値を入れてください'})
    #personal_website = forms.URLField(error_messages={"invalid": "正しいurlを入力してください"})
    """
    IntegerField
    """
    """验证器的使用"""
    # email = forms.CharField(validators=[validators.EmailValidator(
    #     message='正しいメールを入力してください!'
    # )])
    """正規表現のバリデーション"""
    telepone = forms.CharField(validators=[
        validators.RegexValidator(r'0[98]0\d*', message='携帯番号ではない')
    ])

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[
        validators.RegexValidator(r'0[98]0\d{6}', message='携帯番号ではない')
    ])
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # exists存在するかどうか
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message='番号既にある')
        #検証してから返す
        return telephone

    #エラーメッセージの再構築
    #実際使う際に親クラスに入れて、フォームクラス作る時にそれを継承する
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

    #二回パスワード入力あってません
    def clean(self):
       #カラム検証通った後ここまで来る
       cleaned_data = super().clean()
       pwd1 = cleaned_data.get('pwd1')
       pwd2 = cleaned_data.get('pwd2')
       if pwd1 != pwd2:
           raise forms.ValidationError(message='二回の入力あってませんあってません')
       return cleaned_data