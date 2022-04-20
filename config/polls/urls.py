from django.urls import path
from .views import QuestionViewSet,ChoiceViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('q', QuestionViewSet, basename='questions')
router.register('c', ChoiceViewSet, basename='choices')
urlpatterns = router.urls

