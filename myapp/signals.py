from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Appointment

@receiver(post_save, sender=Appointment)
def send_appointment_email(sender, instance, **kwargs):
    if instance.status == 'ACCEPT' or instance.status == 'REJECT':
        subject = f"Appointment {instance.status}ED"
        patient_email = instance.patient.user.email  # Replace 'email' with the actual field name in your Patient model
        context = {
            'status': instance.status,
            'date': instance.date, 
            'time': instance.time
            }

        # Render HTML content from a template
        html_message = render_to_string('myapp/appointment_status_mail.html', context)

        # Send email
        send_mail(
            subject,
            strip_tags(html_message),  # Strip HTML tags for plain text version
            'mathiaswilfred7@yahoo.com',  # Replace with your sender email address
            [patient_email],
            html_message=html_message,
        )
