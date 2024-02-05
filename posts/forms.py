from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'text', 'category']

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control','autocomplete': 'off'})
        
        self.fields['text'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['text'].required = False




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'parent_category', 'image']