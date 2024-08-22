from django.urls import path
from .views import CourseRecommendationView


urlpatterns = [
    path('recommend/', CourseRecommendationView.as_view(), name='course-recommendation'),
]
