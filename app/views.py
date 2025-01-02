from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Instructor, Post

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class CoursePageView(TemplateView):
    template_name = 'app/courses.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/posts_list.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/posts_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'contact_email', 'body']
    template_name = 'app/posts_create.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'contact_email', 'body']
    template_name = 'app/posts_update.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'app/posts_delete.html'
    success_url = reverse_lazy('posts')

class CalendarPageView(TemplateView):
    template_name = 'app/calendar.html'

class OurTeamPageView(TemplateView):
    template_name = 'app/team.html'

class InstructorListView(ListView):
    model = Instructor
    context_object_name = 'instructors'
    template_name = 'app/team.html'

class InstructorDetailView(DetailView):
    model = Instructor
    context_object_name = 'instructor'
    template_name = 'app/team.html'

class InstructorCreateView(CreateView):
    model = Instructor
    fields = ['name', 'bio', 'rating', 'verified_credentials', 'years_of_experience',
              'profile_picture', 'specialties', 'contact_email', 'phone_number']
    template_name = 'app/team_create.html'

class TestimonialPageView(TemplateView):
    template_name = 'app/testimonial.html'

class PagesPageView(TemplateView):
    template_name = 'app/pages.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'