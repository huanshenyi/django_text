from django import forms

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='タイトル:',
                            error_messages={'max_length': '入力できる最大値を超えました', 'min_length': '最小値に満たない'})
    content = forms.CharField(widget=forms.Textarea, label='内容:',
                              error_messages={"required": '内容入力しなければならない'})
    email = forms.EmailField(label='メール:',
                             error_messages={"required": '内容入力しなければならない'})
    reply = forms.BooleanField(required=False, label='解答:')