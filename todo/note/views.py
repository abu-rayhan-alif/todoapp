from django.shortcuts import render
from .models import Notes
# Create your views here.
from .serializers import NotesSerializer
from rest_framework import viewsets 
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter


class NoteSerializerView(viewsets.ModelViewSet):

    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes=[IsAdminUser]
    authentication_classes=[SessionAuthentication]

    filter_backends=[SearchFilter]
    search_fields=['updatetime']
    search_fields=['title']
    filter_class=[SearchFilter]
    filter_backends=[OrderingFilter]

