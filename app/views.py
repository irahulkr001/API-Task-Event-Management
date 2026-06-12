from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView

# Create your views here.
from rest_framework.response import Response
from app.serializers import EventSerializer
from app.models import EventModel


class EventListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        events = EventModel.objects.all()
        stu = EventSerializer(events, many=True)
        return Response(stu.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EventDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return EventModel.objects.get(id=pk)
        except:
            raise Http404
    def get(self,request,pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request,pk):
        event=self.get_object(pk)
        stu=EventSerializer(event,data=request.data)
        if stu.is_valid():
            stu.save()
            return Response(stu.data,status=status.HTTP_200_OK)
        return Response(stu.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        event=self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from app.serializers import UserSerializer
class Register(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer


class Logout(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        request.user.auth_token.delete()
        return Response({'msg':'Logout Successfully'},status=status.HTTP_200_OK)
