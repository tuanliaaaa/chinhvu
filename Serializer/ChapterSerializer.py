from rest_framework import serializers
from Entity.models.Chapter import Chapter
from Entity.models.Film import Film
class FilmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Film
        fields = '__all__'
class ChapterSerializer(serializers.ModelSerializer):
    Film = FilmSerializer(many=False)

    class Meta:
        model = Chapter
        fields = '__all__'
