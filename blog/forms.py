from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "image", "tags", "published"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter blog title"
            }),

            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 10,
                "placeholder": "Write your blog content here..."
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "tags": forms.SelectMultiple(attrs={
                "class": "form-select"
            }),

            "published": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }
