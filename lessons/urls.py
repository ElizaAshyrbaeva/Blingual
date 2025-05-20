from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, WordViewSet, LessonViewSet, UserProfileViewSet, QuestionViewSet, QuizViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'words', WordViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
