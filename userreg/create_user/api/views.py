from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from create_user.api.serializers import Registerserializers

@api_view(['POST',])
def registration_view(request):
    permission_classes = (IsAuthenticated,)
    if request.method=='POST':
        serializer=Registerserializers(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="successfully registered a new user"
            data['email']=account.email
            data['username'] = account.username
        else:
            data=serializer.errors
        return Response(data)

@api_view(['GET',])
def Viewhello_view(request):
    if request.method == 'GET':
        permission_classes = (IsAuthenticated,)
        content={'message':'Hello,World'}
        return Response(content)


