from django.shortcuts import render

from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        email =request.POST['email']
        subject= request.POST['subject']
        message =request.POST['message']

        send_mail(            
                subject,
                message,
                'durgeshtext@gmail.com', # from email
                [email],
                # fail_silently=True,
            )
    
    return render(request, 'index.html')
   
