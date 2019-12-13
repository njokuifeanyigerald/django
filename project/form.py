from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    title = forms.CharField(label="My Title", widget=forms.TextInput(
        attrs={
            "placeholder": "your title",
            "class": "form-control"
        }
    ))  # required=False
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "id": "my_description",
            "rows": 2,
            "cols": 120
        }
    ))
    price = forms.DecimalField(initial=199.99, widget=forms.NumberInput(
        attrs={
            "class": "form-control"
        }
    ))
    email = forms.EmailField(required=False,widget=forms.EmailInput(
        attrs={
            "class": "form-control"
        }
    ))
    summary = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "id": "my_summary",
            "rows": 2,
            "cols": 120
        }
    ))

    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]
    # def clean_title(self):
    #     title =self.cleaned_data.get('title')
    #     if not "country" in title:
    #         raise forms.ValidationError("this is not a valid issue")
    #     if not "programming" in title:
    #         raise forms.ValidationError("this is not a valid issue")
    # def clean_email(self):
    #     email  = self.cleaned_data.get('email')
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("wrong email format")

class RawProjectForm(forms.Form):
    title = forms.CharField(label="My Title", widget=forms.TextInput(
        attrs={
            "placeholder": "your title",
            "class": "form-control"
        }
    ))   #required=False
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "id": "my_description",
            "rows":2,
            "cols": 120
        }
    ))
    price = forms.DecimalField(initial=199.99, widget=forms.NumberInput(
        attrs={
            "class": "form-control"
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control"
        }
    ))
