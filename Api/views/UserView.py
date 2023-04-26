from Entity.models.Role import Role
from Entity.models.User import User
from Entity.models.UserRole import UserRole
from rest_framework.views import APIView
from rest_framework.response import Response
from Serializer.UserSerializer import UserSerializer,UserByAdminSerializer
from datetime import datetime,timedelta,timezone
from django.db.models import Q
import jwt
from core.settings import SECRET_KEY
class Signup(APIView):
    def post(self,request):
        userSerializer = UserSerializer(data=request.data)
        if userSerializer.is_valid():
            user=userSerializer.save()
            exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
            roles=[]
            userRoles=UserRole.objects.filter(User=user)
            for userRole in userRoles:
                roles.append(userRole.Role.RoleName)
            payLoad = {'UserID':user.pk,"Username":user.UserName,"Roles":roles,"exp":exp}
            jwtData = jwt.encode(payLoad,SECRET_KEY,) 
            jwtUser={"access":jwtData}
            return Response(jwtUser,status=201)
        return Response(userSerializer.errors, status=400)

    

