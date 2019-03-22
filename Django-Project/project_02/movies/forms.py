from django import forms
from .models import Movie

class MovieModelForm(forms.ModelForm) :
    class Meta :
        model = Movie
        fields = ['title', 'audience','poster_url','description','genre']
        # TODO : 장르, 포스터 수정
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력해주세요.'
                }),
            'audience': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }),
            'poster_url': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'genre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                })
        }