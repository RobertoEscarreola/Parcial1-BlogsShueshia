from typing import List
from xml.etree.ElementTree import Comment
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Manga, Anime, ReviewAnime, ReviewManga
from .forms import PostForm, ReviewAnimeForm, ReviewMangaForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

""" Vista cuya función es dar likes a los blogs, tomando liked como booleano """
def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


""" Es la vista de la página principal"""
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


""" Esta es una función para filtrar los post dependiendo del su tag """
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})


""" Vista detallada sobre algún post """
class ArticleDetailView(DetailView):
    model= Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(ArticleDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

""" Vista para crear un blog o post a partir de la vista genérica CREATE """
class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    """ fields = '__all__' """

""" Vista para actualizar un blog o post a partir de la vista genérica UPDATE """
class ArticleUpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']


""" Vista para eliminar un blog o post a partir de la vista genérica DELETE """
class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


""" Vista de creación para crear añadir un comentario a un blog """
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


""" Lista para desplegar los mangas almacenados con la vista LIST """
class manga_list(ListView):
    model = Manga
    template_name = 'manga_list.html'


""" Lista para desplegar los animes almacenados con la vista LIST """
class anime_list(ListView):
    model = Anime

    template_name = 'anime_list.html'


""" Vista para mostrar información específica de un manga con DETAILVIEW """
class manga_detailview(DetailView):
    model = Manga

    template_name = 'manga_detailview.html'


""" Vista para mostrar información específica de un anime con DETAILVIEW """
class anime_detailview(DetailView):
    model = Anime

    template_name = 'anime_detailview.html'


""" Vista para añadir una review a un manga """
class AddReviewManga(CreateView):
    model = ReviewManga
    form_class = ReviewMangaForm
    template_name = 'review_manga.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.manga_id = self.kwargs['pk']
        return super().form_valid(form)


""" Vista para añadir una review a un anime """
class AddReviewAnime(CreateView):
    model = ReviewAnime
    form_class = ReviewAnimeForm
    template_name = 'review_anime.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.anime_id = self.kwargs['pk']
        return super().form_valid(form)


""" Vista para mostrar los post en lista """
class Article_List(ListView):
    model = Post
    template_name = 'article_list.html'

""" NOTA: Por cada vista se hace un html """