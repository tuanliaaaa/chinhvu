from django.urls import path
from .views.token import Token
from .views.ChapterView import ChapterHot,RecommendView
from .views.UserView import Signup
from .views.CategoryFilmView import CategoryAllFilm
from .views.FilmViews import FilmSearch
from .views.HistoryView import HistoryUserLogin

urlpatterns = [
    path('Token',Token.as_view()),
    path('Signup',Signup.as_view()),
    path('ChapterHot',ChapterHot.as_view()),
    path('CategoryAllFim',CategoryAllFilm.as_view()),
    path('FindFilm/<str:filmSearch>',FilmSearch.as_view()),
    path('HistoryUserLogin',HistoryUserLogin.as_view()),
    path('Recommend',RecommendView.as_view()),
]