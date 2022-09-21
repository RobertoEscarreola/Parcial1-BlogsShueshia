from django.urls import path
from .views import AddReviewAnime, AddReviewManga, Article_List, ArticleCreateView, Home, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, CategoryView, LikeView, AddCommentView, anime_detailview, anime_list, manga_detailview, manga_list

""" Links para cada view hecha """
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('create_post/', ArticleCreateView.as_view(), name='create_post'),
    path('update_post/<int:pk>', ArticleUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', ArticleDeleteView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('animelist/', anime_list.as_view(), name='anime_list'),
    path('mangalist/', manga_list.as_view(), name='manga_list'),
    path('anime/<int:pk>', anime_detailview.as_view(), name='anime_detail'),
    path('manga/<int:pk>', manga_detailview.as_view(), name='manga_detail'),
    path('manga/<int:pk>/review/', AddReviewManga.as_view(), name='add_review_manga'),
    path('anime/<int:pk>/review/', AddReviewAnime.as_view(), name='add_review_anime'),
    path('articlelist/', Article_List.as_view(), name='article_list')

]

""" NOTA: los path se usan para asignar un nombre a una dirección url """