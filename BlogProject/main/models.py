from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

""" Modelo de categoría, se usa para los tags 
    Su atributo es name
"""
class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')



""" Modelo principal que es Post, tiene la flexibilidad para ser el Blog en sí 
    Sus atributos van desde title, author, etc. 
"""
class Post(models.Model):
    title = models.CharField(max_length=50)
    header_image = models.ImageField(null=True, blank=True, upload_to="blog_images")
    title_tag = models.CharField(max_length=50, default="SHUESHIA Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=10, default='Blog')
    snippet = models.CharField(max_length=30, default='Presiona el link para leer el post!')
    likes = models.ManyToManyField(User, related_name='blog_post')
    """ Función para contar la cantidad de likes """
    def total_likes(self):
        return self.likes.count()
    """ Función para retornar el título y el autor """
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')



""" Modelo de perfil de usuario, para que se tenga un usuario, biografía, y avatar
    Tiene una función para que retorne el usuario
 """
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile_images")

    def __str__(self):
        return str(self.user)
    
""" Modelo de comentario y sus atributos que son post, name y otros
    Tiene una función para que retorne el título del post y su nombre
 """
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


""" Modelo de manga, y sus atributos tales como name, mangaka y demás """
class Manga(models.Model):
    class meta:
        verbose_name_plural = 'Mangas'
        verbose_name = 'Manga'

    name = models.CharField(max_length=50)
    mangaka = models.CharField(max_length=50, blank=False, null=False)
    genre = models.CharField(max_length=50, blank=False, null=False)
    first_publication = models.DateField()
    chapters = models.IntegerField()
    last_publication = models.DateField()
    synopsis = models.TextField()
    manga_pic = models.ImageField(blank=False, upload_to="manga_pics")
    """ Función para que retorne el nombre """
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


""" Modelo de anime, y sus atributos como name, mangaka, etc """
class Anime(models.Model):
    class meta:
        verbose_name_plural = 'Animes'
        verbose_name = 'Anime'

    name = models.CharField(max_length=50)
    mangaka = models.CharField(max_length=50, blank=False, null=False)
    genre = models.CharField(max_length=50, blank=False, null=False)
    publicationdate = models.DateField()
    enddate = models.DateField()
    episodes = models.IntegerField()
    synopsis = models.TextField()
    anime_pic = models.ImageField(blank=False, upload_to="anime_pics")
    """ Función que retorna el nombre """
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

""" Modelo para hacer una review a un manga y sus atributos como nombre, cuerpo, etc. """
class ReviewManga(models.Model):
    review = models.ForeignKey(Manga, null=True, related_name="mangarevs", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    """ Funcion que retorna la review y el nombre """
    def __str__(self):
        return '%s - %s' % (self.review, self.name)


""" Modelo para hacer una review a un anime y sus atributos como nombre, cuerpo. etc. """
class ReviewAnime(models.Model):
    review = models.ForeignKey(Anime, null=True, related_name="animerevs", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    """ Funcion que retorna la review y el nombre """
    def __str__(self):
        return '%s - %s' % (self.review, self.name)


""" Nota son como clases y sus atributos """