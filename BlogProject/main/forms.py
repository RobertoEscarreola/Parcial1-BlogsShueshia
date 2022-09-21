from django import forms
from .models import Post, Category, Comment, ReviewAnime, ReviewManga

""" Categorías o tags para desplegar y elegir al crear un post
    Su función es filtrar por tags
 """
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


""" Formulario para crear un post, tiene atributos como título, tag, autor, cuerpo, etc.
    También tienen bootstrap para darle formato que es el form-control
 """
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category' , 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list , attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


""" Formulario para actualizar un post, tiene atributos como título, tag, autor, cuerpo, etc.
    También tienen bootstrap para darle formato que es el form-control """
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


""" Formulario para crear comentarios y tiene dos atributos que son nombre y cuerpo y el form-control 
    para el formato
 """
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'nameR': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
    
        }

""" Formulario para crear reviews de manga y tiene dos atributos que son nombre y cuerpo y el form-control 
    para el formato """
class ReviewMangaForm(forms.ModelForm):
    class Meta:
        model = ReviewManga
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
    
        }

""" Formulario para crear reviews de anime y tiene dos atributos que son nombre y cuerpo y el form-control 
    para el formato """
class ReviewAnimeForm(forms.ModelForm):
    class Meta:
        model = ReviewAnime
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
    
        }


""" NOTA: estos formularios se usan como indicativo de una vista """