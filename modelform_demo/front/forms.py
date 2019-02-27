from django import forms
from .models import Book, User

class AddBookForm(forms.ModelForm):
    #検証通過後の検証追加
    # def clean_page(self):
    #     page = self.cleaned_data.get('page')
    #     if page >100:
    #         raise forms.ValidationError('ページ100を超えてはならない!')
    #     return cleaned_data

    class Meta:
        model = Book
        """すべてカラムを検証"""
        fields = '__all__'
        """指定カラムの検証"""
        #fields = ['title', 'page']
        """指定カラムの反対指定"""
        #exclude = ['price']

        """エラーメッセージ"""
        error_messages = {
            'page': {
                'required': 'pageパラメータを入れてください',
                'invalid': '使えるpageパラメータを入力してください'
            },
            'title': {
                'max_length': 'titleの長さ100以内'
            },
            'price': {
                'required': 'priceパラメータを入れてください'
            }
        }

class RegisterForm(forms.ModelForm):
    """新規ユーザーのシミュレーション"""
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('二回入力があってません')
        return cleaned_data
    class Meta:
        model = User
        exclude = ['password']
