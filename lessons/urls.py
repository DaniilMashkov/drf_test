from django.urls import path
from lessons.views import LessonListView, LessonCreateAPIView, LessonDestroyAPIView


urlpatterns = [
    path('', LessonListView.as_view(), name='lessons'),
    path('<int:pk>/', LessonListView.as_view(), name='update_retrieve'),
    path('create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
]