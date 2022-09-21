from django.contrib import admin
from .models import Post, Category, Profile, Comment, Anime, Manga, ReviewAnime, ReviewManga

""" A traves de admin se hacen los registros de los modelos y estos aparecen en admin en la web """
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Anime)
admin.site.register(Manga)
admin.site.register(ReviewManga)
admin.site.register(ReviewAnime)

