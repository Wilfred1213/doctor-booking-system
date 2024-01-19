from myapp.models import Subscription
from django.contrib import messages

def subscription(request):
    if request.method =='POST' and 'email' in request.POST:
        email = request.POST.get('email')
        
        if Subscription.objects.filter(email = email).exists():
            messages.info(request, 'Someone has already subscribe with this email')
        
        else:
            subscribe, created=Subscription.objects.get_or_create(email = email)
            messages.error(request, 'Thank you for subscribing to our news letter')

    