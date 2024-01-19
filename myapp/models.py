from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
TIME_CHOICES = (
        ('8:00 AM - 9:00 AM', '8:00 AM - 9:00 AM' ),
        ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM' ),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM' ),
        ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM' ),
        ('12:00 PM - 1:00 PM', '12:00 PM - 1:00 PM' ),
        ('1:00 PM - 2:00 PM', '1:00 PM - 2:00 PM' ),
        ('2:00 PM - 3:00 PM', '2:00 PM - 3:00 PM' ),
        ('3:00 PM - 4:00 PM', '3:00 PM - 4:00 PM' ),
        ('4:00 PM - 5:00 PM', '4:00 PM - 5:00 PM' )
    )

DEPARTMENT_CHOICES = (
    ('Surgery Department', 'Surgery Department'),
    ('Outpatient', 'Outpatient'),
    ('Inpatient', 'Inpatient'),
    ('Intensive Care Unit', 'Intensive Care Unit'),
    ('Cardiology', 'Cardiology'),
    ('Neurology', 'Neurology'),
    ('Psychiatry', 'Psychiatry'),
    ('Radiology', 'Radiology'),
    ('Laboratory', 'Laboratory'),
    ('Pharmacy', 'Pharmacy'),
    ('Rehabilitation', 'Rehabilitation'),
    ('Hematology', 'Hematology'),
    ('Pediatrics', 'Pediatrics'),
    ('Oncology', 'Oncology'),
    ('Ophthalmology', 'Ophthalmology')
)

CATEGORY_CHOICE= (
    ('Medicine', 'Medicine'),
    ('Equipment', 'Equipment'),
    ('Heart', 'Heart'),
    ('Free Counselling', 'Free Counselling'),
    ('Lab Test', 'Lab Test'),
    
)

class Category(models.Model):
    name = models.CharField(max_length = 255, choices=CATEGORY_CHOICE, null = True)

    def __str__(self):
        return self.name

class Department(models.Model):
    specialization = models.CharField(max_length=255, choices = DEPARTMENT_CHOICES)
    description=models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='department_images', null = True)

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""
        
    def __str__(self):
        return self.specialization
    
    
class Time(models.Model):
    time = models.CharField(max_length = 255, choices = TIME_CHOICES, default = '8:00 AM - 9:00 AM')
    def __str__(self):
        return self.time
    
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null = True)
    image = models.ImageField(upload_to='doctor_images', null = True)
    description=models.CharField(max_length=1000, null=True)

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""
        
    def __str__(self):
        return  (f'{self.user}')

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()
    
class Appointment(models.Model):
    STATUS = [
        ('REJECT', 'Reject'),
        ('ACCEPT', 'Accept'),
        ('PENDING', 'Pending')
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Department, on_delete=models.CASCADE, null = True)
    date = models.DateField()
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null = True)
    message = models.TextField(max_length= 10000, null = True)

    status = models.CharField(max_length = 50, choices = STATUS, default = 'PENDING')
    treated = models.BooleanField(default = False)

    def __str__(self):
        return  (f'Booked for doctor -{self.doctor}')
    
    class Meta:
        ordering = ['-patient',]
    
    def is_available(self):
        return not Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date, time = self.time
        ).exists()

class Service(models.Model):
    name =models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='doctor_images', null = True)
    description=models.CharField(max_length=1000, null=True)

    def __str__(self):
       return self.name

class Blog(models.Model):
    title =models.CharField(max_length=255, null=True)
    description=models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='blog_images', null = True)
    quote = models.CharField(max_length=1000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)

    def imageUrl(self):
        if self.image:
            return self.image.url
        return ''
    
    def cat_count(self):
        return  Category.objects.filter(id=self.category.id).count()
         

    def __str__(self):
       return self.title
    class Meta:
        ordering = ['-date']

class Tag(models.Model):
    title =models.CharField(max_length=255, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content =models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add = True)

class Partners(models.Model):
    description = models.CharField(max_length=1000, null=True)
    logos = models.ImageField(upload_to='partners_images', null = True)
    

    def __str__(self):
        return self.description
    
class Contact(models.Model):
    fullname = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=16, null=True)
    message= models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (f'{self.fullname} -- {self.subject}')
    
class Subscription(models.Model):
    email = models.EmailField(max_length=255)