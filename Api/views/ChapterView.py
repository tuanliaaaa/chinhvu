from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from Entity.models.Film import Film
from Entity.models.History import History
from Entity.models.Category import Category
from Entity.models.Chapter import Chapter
from Entity.models.Actor import Actor
from Serializer.FilmSerializer import FilmSerializer
from Serializer.ChapterSerializer import ChapterSerializer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from django.db.models import Count
from core.roleLoginDecorater import RoleRequest
from django.utils.decorators import method_decorator
class ChapterHot(APIView):
    @method_decorator(RoleRequest(allowedRoles=['Admin','NormalUser']))
    def get(self,request):
        chapterHotCount = History.objects.values('Chapter__id').annotate(count=Count('id')).order_by('-count')
        try:
            chapter = Chapter.objects.get(pk=chapterHotCount[0]['Chapter__id'])
            chapterSerializer =ChapterSerializer(chapter)
            return Response(chapterSerializer.data,status=200)
        except:
            return Response("[]",status=200)



class RecommendView(APIView):
    @method_decorator(RoleRequest(allowedRoles=['Admin','NormalUser']))
    def get(self, request):
        
        history= History.objects.filter(User__id=request.userID)
        #----------------------- Content Based System Recommend -----------------------------
        #khởi tạo lượt xem của người dùng với thể loại
        categoryUserView=[]
        for i in history:
            for j in i.Chapter.Film.filmcategory.all():
                categoryUserView.append(j.Category.id)
        #khởi tạo lượt xem của người dùng với diễn viên
        actorUserView=[]
        for i in history:
            for j in i.Chapter.chapteractor.all():
                actorUserView.append(j.Actor.id)
        #láy toàn bộ chapter User chưa xem 
        chapterAll = Chapter.objects.exclude(id__in=history.values_list('Chapter', flat=True))
        #lấy toàn bộ Thể loại
        categoryAll = Category.objects.all()

        #lấy toàn bộ diễn viên
        actorAll =Actor.objects.all()
        #khởi tạo ma trận với hàng là các chapter còn bảng là category,actor
        chapter_matrix = np.zeros((len(chapterAll), len(categoryAll)+len(actorAll)))
        # khởi tạo phần category cho chapter_matrix
        for i in range(len(chapterAll)):
            for j in range(len(categoryAll)):
                if categoryAll[j] in [ i.Category for i in chapterAll[i].Film.filmcategory.all()]:
                    chapter_matrix[i,j]=1
        # khởi tạo phần actor cho chapter_matrix
        for i in range(len(chapterAll)):
            for j in range(len(actorAll)):
                if actorAll[j] in [ i.Actor for i in chapterAll[i].chapteractor.all()]:
                    chapter_matrix[i,j]=1
                    
        #khởi tạo ma trận với hàng là User đang đang nhập(1 hàng) còn bảng là category,actor
        userLogin_matrix = []
        # khởi tạo phần category cho userLogin_matrix
        for i in categoryAll:
            if i.id in categoryUserView:
                userLogin_matrix.append(categoryUserView.count(i.id)/len(categoryUserView))
            else:
                userLogin_matrix.append(0)
        # khởi tạo phần actor cho userLogin_matrix
        for i in actorAll:
            if i.id in actorUserView:
                userLogin_matrix.append(actorUserView.count(i.id)/len(actorUserView))
            else:
                userLogin_matrix.append(0)
        similarity_scores = cosine_similarity( np.array(userLogin_matrix).reshape(1,-1),chapter_matrix)
        sorted_indices = np.argsort(similarity_scores, axis=1)[0]
        
        # Lấy ra các chapter được recommend
        recommended_chapters = []
        for i in sorted_indices:
            if chapterAll[int(i)].ChapterStatus =='Đã Ra':
                recommended_chapters.append(chapterAll[int(i)])
        
        chapterRecommendSerializer= ChapterSerializer(recommended_chapters,many=True)
      
        return Response(chapterRecommendSerializer.data, status=status.HTTP_200_OK)
