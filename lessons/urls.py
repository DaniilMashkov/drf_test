from django.urls import path
from lessons.views import LessonListView, LessonCreateAPIView, LessonRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', LessonListView.as_view(), name='lessons'),
    path('create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('rud/<int:pk>', LessonRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_delete')
]