from Entity.models.User import User
from Entity.models.Chapter import Chapter
from Entity.models.History import History
from rest_framework.views import APIView
from rest_framework.response import Response
from Serializer.HistorySerializer import UserChaptersSerializer,HistorySerializer
import jwt
from core.roleLoginDecorater import RoleRequest
from django.utils.decorators import method_decorator
from core.settings import SECRET_KEY
class HistoryUserLogin(APIView):
    @method_decorator(RoleRequest(allowedRoles=['NormalUser']))
    def get(self,request):
        try:
            historyUserLogin = User.objects.get(pk=request.userID)
            historyUserLoginJson = UserChaptersSerializer(historyUserLogin)
        except: 
            return Response({"massage":"user không tồn tại"},status=204)
        return Response(historyUserLoginJson.data,status=200)

        
