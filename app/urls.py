from django.urls import path
from .views import (HomePageView, AboutPageView, CoursePageView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CalendarPageView,
                    OurTeamPageView, TestimonialPageView, PagesPageView, ContactPageView,
                    InstructorListView, InstructorDetailView, InstructorCreateView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('course/', CoursePageView.as_view(), name='course'),
    path('', PagesPageView.as_view(), name='pages'),

    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts_detail'),
    path('posts/create', PostCreateView.as_view(), name='posts_create'),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='posts_delete'),

    path('calendar/', CalendarPageView.as_view(), name='calendar'),
    path('team/', OurTeamPageView.as_view(), name='team'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('team/', InstructorListView.as_view(), name='team'),
    path('team/<int:pk>/', InstructorDetailView.as_view(), name='team_detail'),
    path('team/create', InstructorCreateView.as_view(), name='team_create'),
]