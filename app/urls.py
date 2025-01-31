from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import (
    HomePageView, AboutPageView, CoursePageView, DatabasePageView, UserCreateView, UserUpdateView, LoginPage,
    UserDeleteView, PostListView, PostDetailView, AdminPostCreateView, PostCreateView, PostUpdateView,
    PostDeleteView, CourseCreateView, CourseUpdateView, CourseDeleteView, AdminEnrollmentCreateView, EnrollmentCreateView,
    EnrollmentUpdateView, EnrollmentDeleteView, CalendarPageView, OurTeamPageView, TestimonialPageView, PagesPageView,
    ContactPageView, InstructorListView, InstructorDetailView, InstructorCreateView, InstructorUpdateView, InstructorDeleteView,
    AdminInstructorCreateView
)

urlpatterns = [
    path('', LoginPage.as_view(), name='login'),
    path('login/', views.User_login, name='user_login'),
    path('register/', views.register_User, name='user_register'),
    path('admins/', views.admin_login, name='admin_login'),

    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('course/', CoursePageView.as_view(), name='course'),
    path('pages/', PagesPageView.as_view(), name='pages'),

    path('database/', DatabasePageView.as_view(), name='database'),

    path('usercreate/create/', UserCreateView.as_view(), name='user_create'),
    path('userupdate/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('userdelete/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts_detail'),
    path('database/create/', AdminPostCreateView.as_view(), name='admin_post_create'),
    path('posts/create/', PostCreateView.as_view(), name='posts_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='posts_delete'),

    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    path('adminenrollment/create/', AdminEnrollmentCreateView.as_view(), name='admin_enrollment_create'),
    path('enrollment/create/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollment/<int:pk>/edit/', EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('enrollment/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment_delete'),

    path('calendar/', CalendarPageView.as_view(), name='calendar'),
    path('our-team/', OurTeamPageView.as_view(), name='our_team'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('team/', InstructorListView.as_view(), name='team'),
    path('team/<int:pk>/', InstructorDetailView.as_view(), name='team_detail'),
    path('team/create/', InstructorCreateView.as_view(), name='about_instructor_create'),
    path('team/<int:pk>/edit/', InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructordelete/<int:pk>/delete/', InstructorDeleteView.as_view(), name='instructor_delete'),
    path('admin_instructor/create/', AdminInstructorCreateView.as_view(), name='instructor_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
