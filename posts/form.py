from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'banner', 'slug']
        """
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Content',
            'slug': 'URL Slug',
        }
        help_texts = {
            'slug': 'A unique identifier for the post, used in the URL.',
        }
        """