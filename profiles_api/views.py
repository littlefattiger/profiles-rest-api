from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request, format = None):
        """return a lilst of APIView feature"""
        an_apiview =[
        'Uses HTTP methods as function (get, post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Give you the most control over your application logic',
        'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    def post(self, request):
        """create a hello message with our name"""
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def put(self, request,pk=None):
        """handling updating an object"""
        return Response({'method':'Put!'})

    def patch(self, request,pk=None):
        """Partially handling updating an object"""
        return Response({'method':'PATCH'})
    def delete(self, request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
class HelloViewSet(viewsets.ViewSet):
    """test api view set"""
    serializer_class = serializers.HelloSerializer



    def list(self,request):
        a_viewset = [
        'Uses actions (list, create,retrive,update,partial_update)',
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code',

        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})
    def create(self,request):
        """Create Hello Function"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request,pk=None):
        """handle getting an object by its ID"""

        return Response({'Http_method':'Get'})
    def update(self, request,pk=None):
        """handle getting an object by its ID"""

        return Response({'Http_method':'Put'})
    def partial_update(self, request,pk=None):
        """handle getting an object by its ID"""

        return Response({'Http_method':'Partial Put'})
    def destroy(self, request,pk=None):
        """handle getting an object by its ID"""

        return Response({'Http_method':'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """test api view set from model viewset"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_class = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
