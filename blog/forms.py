from .models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# Apply summernote to specific fields.
class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())


class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ('title', 'image')
