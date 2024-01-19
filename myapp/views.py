
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.db.models import Q, Count
from myapp.search import search, pagination, sidebar, comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from authentications.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date
from myapp.sub import subscription

User = get_user_model

def about(request):
    department = Department.objects.all()[:6]
    doctor = Doctor.objects.all()[:6]
    comment = Comment.objects.all()
    partners = Partners.objects.all()

    subscription(request)
    context = {
        'departments':department,
        'doctors':doctor,
        'comments':comment,
        'partners':partners,
    }
    return render(request, 'myapp/about.html', context)

def category_detail(request, cat_detail):
    cat_id = Category.objects.get(id = cat_detail)

    blog = Blog.objects.filter(category = cat_id)

    # paginator
    blogs = pagination(request, blog)


    search_comment = search(request)

    # Annotate each blog with the count of comments
    blog_with_comment_count = blog.annotate(comment_count=Count('comment'))

    # side bar category count
    categories_with_blog_count = Category.objects.annotate(blog_count=Count('blog'))

    grouped_blogs = {}
    
    for blog_post in blog_with_comment_count :
        comment_count = blog_post.comment_count
        if comment_count not in grouped_blogs:
            grouped_blogs[comment_count] = []
        grouped_blogs[comment_count].append(blog_post)


    # Select the top posts from each group
    popular_posts = []
    for comment_count, posts in sorted(grouped_blogs.items(), reverse=True):
        popular_posts.extend(posts[:3])



    context = {
        'blogs':blogs,
        'searches': search_comment,
        'popular': popular_posts,
        'categories':categories_with_blog_count,
        'blog':blog,
    }
    return render(request, 'myapp/category_detail.html', context)


def index(request):
    app_doctor = Appointment.objects.all()
    
    times = Time.objects.all()
    partners = Partners.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST' and 'department' in request.POST:
        department = request.POST.get('department')
        doctor_id = request.POST.get('doctor')

        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        
        user = request.user

        patient, created = Patient.objects.get_or_create(user=user)
        department, created = Department.objects.get_or_create(specialization=department)
        times, created = Time.objects.get_or_create(time=time)
        doctor, created = Doctor.objects.get_or_create(id=doctor_id)
        # subscription(request)
        
        
        appointment = Appointment(
            doctor=doctor,
            patient=patient,
            date=date,
            specialization=department,
            time=times,
            message=message
        )

        if appointment.is_available():
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('confirmation')
            # return JsonResponse({'status': 'success'})
        else:
            messages.error(request, 'Sorry, the selected time is already booked.')
            return redirect('index')
            # return JsonResponse({'status': 'error', 'message': 'Time already booked'})
    subscription(request)

    doctors = Doctor.objects.filter(user__is_doctor=True)
    
    for dept in doctors:
        Doctor.objects.filter(department = dept.department)
        print('doctors', CustomUser.objects.filter(is_doctor = True))
    


    context = {
        'appointment': app_doctor,
        'doctors': doctors,
        'departments': departments,
        'times': times,
        'partners':partners,
        'partners_des':partners.first(),
        
    }
    return render(request, 'myapp/index.html', context)

@login_required(login_url='authentications:login_view')
def appointment(request):
    
    app_doctor = Appointment.objects.all()
    
    doctors = Doctor.objects.filter(user__is_doctor=True)
    
    for dept in doctors:
        Doctor.objects.filter(department = dept.department)
        print('doctors', CustomUser.objects.filter(is_doctor = True))

    times = Time.objects.all()
    departments = Department.objects.all()

    
    print('all doctores', CustomUser.objects.filter(is_doctor = True))

    if request.method == 'POST' and 'department' in request.POST:
        department = request.POST.get('department')
        doctor_id = request.POST.get('doctor')

        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Check if the selected time is available
        user = request.user

        patient, created = Patient.objects.get_or_create(user=user)
        department, created = Department.objects.get_or_create(specialization=department)
        times, created = Time.objects.get_or_create(time=time)
        doctor, created = Doctor.objects.get_or_create(id=doctor_id)
        
        appointment = Appointment(
            doctor=doctor,
            patient=patient,
            date=date,
            specialization=department,
            time=times,
            message=message,
           
            

        )

        if appointment.is_available():
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('confirmation')
        else:
            messages.error(request, 'Sorry, the selected time is already booked.')
            return redirect('appointment')
    subscription(request)

    context = {
        'appointment': app_doctor,
        'doctors': doctors,
        'departments': departments,
        'times': times
    }
    
    return render(request, 'myapp/appointment.html', context)

def confirmation(request):
    return render(request, 'myapp/confirmation.html', {})


def department(request):
    department = Department.objects.all()[:6]

    context = {
        'departments':department
    }
    return render(request, 'myapp/department.html', context)


def department_detail(request, department_id):
    dept_id = Department.objects.get(id = department_id)

    subscription(request)

    context = {
        'department':dept_id
    }
    return render(request, 'myapp/department-single.html', context)


def doctor(request):
    department = Department.objects.all()[:6]
    doctor = Doctor.objects.all()[:6]

    subscription(request)
    context = {
        'departments':department,
        'doctors':doctor
    }
    return render(request, 'myapp/doctor.html', context)


def doctor_detail(request, doctor_id):
    subscription(request)
    doctorid = Doctor.objects.get(id = doctor_id)

    context = {
        'doctor':doctorid
    }
    return render(request, 'myapp/doctor-single.html', context)


def service(request):
    subscription(request)
    service = Service.objects.all()
    context = {
        'services':service,
    }
    return render(request, 'myapp/service.html', context)


def blog(request):
    subscription(request)
    blog = Blog.objects.all()
    tag = Tag.objects.all()


    categories_with_blog_count = Category.objects.annotate(blog_count=Count('blog'))

    # popular posts
    popular_posts =sidebar(request)
    # Pagination
    blogs = pagination(request, blog)

    search_comment = search(request)

    context = {
        'blogs': blogs,
        'searches': search_comment,
        'popular': popular_posts,
        'categories':categories_with_blog_count,
        'tags':tag,
        
    }
    return render(request, 'myapp/blog-sidebar.html', context)

def tags(request, blog_id):
    
    blog = Blog.objects.get(id = blog_id)
    tag = Tag.objects.filter(blog = blog)
    comments = blog.comment_set.all()
    # Pagination
    blogs = pagination(request, tag)

    categories_with_blog_count = Category.objects.annotate(blog_count=Count('blog'))
    comment(request, blog)
    # popular posts
    popular_posts =sidebar(request)
    
    search_comment = search(request)
    context = {
        'tags':tag,
        'blogs': blogs,
        'searches': search_comment,
        'popular': popular_posts,
        'categories':categories_with_blog_count,
        'comments':comments,
        }
    return render(request, 'myapp/all_tags.html', context)

def blog_detail(request, blog_id):
    user = request.user
    tag = Tag.objects.all()
    blog = Blog.objects.get(id=blog_id)
    comments = blog.comment_set.all()
   
    count_comment = Comment.objects.filter(blog=blog).count()
    comment(request, blog)
    
    search_comment = search(request)
    subscription(request)

    categories_with_blog_count = Category.objects.annotate(blog_count=Count('blog'))

    # popular posts
    popular_posts =sidebar(request)
    
    search_comment = search(request)

    context = {
        'blog':blog,
        'comments':comments,
        'count':count_comment,
        'searches':search_comment,
        'popular': popular_posts,
        'categories':categories_with_blog_count,
        'tags':tag,
    }

    return render(request, 'myapp/blog-single.html', context)

    
@login_required(login_url='authentications:login_view')

def view_appointment(request):
    # Get the currently logged-in user
    user = request.user
    today = date.today()
    
    upcoming_appointments = Appointment.objects.filter(patient__user=user, treated=False, date__gte=today)


    try:
        doctor = Doctor.objects.get(user=user)
    except Doctor.DoesNotExist:
        doctor =None

    # Filter appointments based on the logged-in doctor
    appointments = Appointment.objects.filter(doctor=doctor)
    print('Appointments:', appointments)


    context = {
        'appointments': appointments,
        'upcoming':upcoming_appointments
    }
    return render(request, 'myapp/view_appointment.html', context)

@login_required(login_url='authentications:login_view')
def accept_appointment(request, patient_id):
    appointment = get_object_or_404(Appointment, id=patient_id)

    if appointment.status == 'PENDING':
        appointment.status = 'ACCEPT'
        
        appointment.save()
        messages.info(request, 'You accepted this appointment')
    else:
        messages.warning(request, 'This appointment cannot be accepted.')

    return redirect(reverse('view_appointment'))

@login_required(login_url='authentications:login_view')
def reject_appointment(request, patient_id):
    appointment = get_object_or_404(Appointment, id=patient_id)

    if appointment.status == 'PENDING':
        appointment.status = 'REJECT'
        appointment.save()
        messages.info(request, 'You Rejected this appointment')
    else:
        messages.warning(request, 'This appointment cannot be Rejected.')

    return redirect(reverse('view_appointment'))
    
def treated_appointment(request, patient_id):
    appointment = get_object_or_404(Appointment, id=patient_id)

    if appointment.treated == False:
        appointment.treated = True
        appointment.save()
        messages.info(request, 'This appointment is treated')
    else:
        messages.warning(request, 'Error while marking this appointment as treated.')

    return redirect(reverse('view_appointment'))

def contact(request):
    subscription(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        subject= request.POST.get('subject')
        email= request.POST.get('email')
        message= request.POST.get('message')
        phone= request.POST.get('phone')

        user_data, created = Contact.objects.get_or_create(
            fullname =name,
            subject = subject,
            email = email,
            message = message, 
            phone = phone,
        )
        user_data.save()
        messages.info(request, 'Thank you for contacting us. We will get back to you')
        return redirect('contact')
        # return JsonResponse({'status': 'success'})
    
    return render(request, 'myapp/contact.html')


