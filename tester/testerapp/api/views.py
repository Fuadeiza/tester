from rest_framework import generics
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from testerapp.models import testQuestions
from .serializers import testQuestionsSerializer


class testQuestionsViewset(ModelViewSet):
    queryset= testQuestions.objects.all()
    serializer_class =testQuestionsSerializer
    # lookup_field='id'