from django import forms
from .models import ClassApp
class ClassAppForm(forms.ModelForm):
    title = forms.CharField( widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 2,
            "cols": 120
        }
    ))
    price = forms.CharField(widget=forms.NumberInput(
        attrs={
            "class": "form-control"
        }
    ))
    summary = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 2,
            "cols": 120,
            "class": "form-control"
        }
    ))
    remember = forms.BooleanField(widget=forms.NullBooleanSelect(
        attrs={
            "class": "form-control"
        }
    ))
    class Meta:
        model = ClassApp
        fields = {
            "title",
            "description",
            "price",
            "summary",
            "remember"
        }
class ClassAppRawForm(forms.Form):
    title = forms.CharField(label="title", widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 2,
            "cols": 120
        }
    ))
    price = forms.CharField(widget=forms.NumberInput(
        attrs={
            "class":"form-control"
        }
    ))
    summary = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows":2,
            "cols": 120,
            "class": "form-control"
        }
    ))
    remember = forms.BooleanField(widget=forms.NullBooleanSelect(
        attrs={
            "class": "form-control"
        }
    ))