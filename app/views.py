from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Post, Course, Enrollment, Instructor, Admin
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now


# LOGIN

class LoginPage(TemplateView):
    template_name = "registration/login.html"


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(username=username)
            if admin.password == password:
                request.session['admin_id'] = admin.id
                request.session['admin_firstname'] = admin.firstname
                messages.success(request, "Admin login successful.")
                return redirect('database')
            else:
                messages.error(request, "Invalid username or password.")
        except Admin.DoesNotExist:
            messages.error(request, "Admin does not exist. Please contact support.")

    return render(request, 'registration/admin_login.html')


def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        except User.DoesNotExist:
            messages.error(request, "Customer does not exist. Please register first.")

    return render(request, 'registration/login.html')


def register_User(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('user_register')

        user = User(
            name=name,
            username=username,
            email=email,
            password=password,
        )
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'registration/register.html')


class DatabasePageView(TemplateView):
    template_name = 'app/database.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['posts'] = Post.objects.all()
        context['courses'] = Course.objects.all()
        context['enrollments'] = Enrollment.objects.all()
        context['instructors'] = Instructor.objects.all()

        context['total_users'] = User.objects.count()
        context['total_instructors'] = Instructor.objects.count()

        # Safely get the most recent user
        try:
            context['recent_user'] = User.objects.latest('id')
        except ObjectDoesNotExist:
            context['recent_user'] = None  # Default to None if no users exist

        # Safely get the most recent post
        try:
            context['recent_post'] = Post.objects.latest('id')
        except ObjectDoesNotExist:
            context['recent_post'] = None  # Default to None if no posts exist
        return context


class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class CoursePageView(TemplateView):
    template_name = 'app/courses.html'


class UserCreateView(CreateView):
    model = User
    fields = ['name', 'username', 'password', 'email']
    template_name = 'app/user_create.html'

    def get_success_url(self):
        return reverse_lazy('database')


class UserUpdateView(UpdateView):
    model = User
    fields = ['name', 'username', 'password', 'email']
    template_name = 'app/user_update.html'

    def get_success_url(self):
        return reverse_lazy('database')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'app/user_delete.html'

    def get_success_url(self):
        return reverse_lazy('database')


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/posts_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/posts_detail.html'


class AdminPostCreateView(CreateView):
    model = Post
    fields = ['user', 'body']
    template_name = 'app/admin_post_create.html'

    def get_success_url(self):
        return reverse_lazy('database')


class PostCreateView(CreateView):
    model = Post
    fields = ['user', 'body']
    template_name = 'app/posts_create.html'

    def get_success_url(self):
        return reverse_lazy('posts')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'contact_email', 'body']
    template_name = 'app/posts_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'app/posts_delete.html'

    def get_success_url(self):
        return reverse_lazy('database')


class CourseCreateView(CreateView):
    model = Course
    fields = ['course_type', 'description', 'duration', 'instructor']
    template_name = 'app/course_create.html'

    def get_success_url(self):
        return reverse_lazy('database')


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_type', 'description', 'duration', 'instructor']
    template_name = 'app/course_update.html'

    def get_success_url(self):
        return reverse_lazy('database')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'app/course_delete.html'

    def get_success_url(self):
        return reverse_lazy('database')


class AdminEnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ['user', 'course', 'enrollment_date',]
    template_name = 'app/admin_enrollment_create.html'

    def get_success_url(self):
        return reverse_lazy('database')


class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ['user', 'course', 'enrollment_date',]
    template_name = 'app/enrollment_create.html'

    def get_success_url(self):
        return reverse_lazy('course')


class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    fields = ['user', 'course', 'enrollment_date', 'enrollment_status']
    template_name = 'app/enrollment_update.html'

    def get_success_url(self):
        return reverse_lazy('database')


class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'app/enrollment_delete.html'

    def get_success_url(self):
        return reverse_lazy('database')


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
    template_name = 'app/team_detail.html'


class InstructorCreateView(CreateView):
    model = Instructor
    fields = ['name', 'bio', 'verified_credentials', 'years_of_experience',
              'profile_picture', 'specialties', 'contact_email', 'phone_number']
    template_name = 'app/about_instructor_create.html'

    def get_success_url(self):
        return reverse_lazy('team')


class InstructorUpdateView(UpdateView):
    model = Instructor
    fields = ['name', 'bio', 'verified_credentials', 'years_of_experience',
              'profile_picture', 'specialties', 'contact_email', 'phone_number']
    template_name = 'app/instructor_update.html'

    def get_success_url(self):
        return reverse_lazy('database')


class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'app/instructor_delete.html'

    def get_success_url(self):
        return reverse_lazy('database')


class AdminInstructorCreateView(CreateView):
    model = Instructor
    fields = ['name', 'bio', 'verified_credentials', 'years_of_experience',
              'profile_picture', 'specialties', 'contact_email', 'phone_number']
    template_name = 'app/instructor_create.html'

    def get_success_url(self):
        return reverse_lazy('database')


class TestimonialPageView(TemplateView):
    template_name = 'app/testimonial.html'


class PagesPageView(TemplateView):
    template_name = 'app/pages.html'


class ContactPageView(TemplateView):
    template_name = 'app/contact.html'
