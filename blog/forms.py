from django import forms

from .models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('Title은 3글자 이상 입력해 주세요!')


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)
