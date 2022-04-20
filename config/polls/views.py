from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class QuestionViewSet(viewsets.ModelViewSet):
    queryset=models.Question.objects.all()
    serializer_class= serializers.QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset=models.Choice.objects.all()
    serializer_class= serializers.ChoiceSerializer
