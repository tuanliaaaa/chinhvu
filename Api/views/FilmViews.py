from Entity.models.Film import Film
from Entity.models.Category import Category
from Entity.models.Chapter import Chapter
from Entity.models.CategoryFilm import CategoryFilm
from Serializer.ChapterSerializer import ChapterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from core.settings import MEDIA_ROOT,BASE_DIR
import os
from datetime import datetime
import json
from core.roleLoginDecorater import RoleRequest
from django.utils.decorators import method_decorator
from Serializer.FilmSerializer import FilmSerializer
from Serializer.CategoryFilmSerializer import FilmCategorysSerializer
class FilmSearch(APIView):
    @method_decorator(RoleRequest(allowedRoles=['Admin','NormalUser']))
    def get(self,request,filmSearch):
        film = Film.objects.filter(Q(FilmName__icontains=filmSearch)|Q(chapters__ChapterName__icontains=filmSearch)|Q(chapters__ChapterDescription__icontains=filmSearch)).distinct()
        filmserializer = FilmSerializer(film,many=True)
        return Response(filmserializer.data,status=200)


