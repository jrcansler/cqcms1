from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
import smtplib
# Create your views here.

def index(request):
        return render(request, 'index.html')

def about(request):
        return render(request, 'about.html')

def contact(request):
    form = forms.UserForm()

    if request.method == 'POST':
            first = request.POST.get('firstname')
            email2 = request.POST.get('email2')
            email1 = request.POST.get('email')
            company = request.POST.get('company')
            comment = request.POST.get('comment')

            if email1 == email2:

                email = 'vetautoreport@gmail.com'
                password = 'Jacobs2066'
                send_to_email = ['jacobcansler@gmail.com', 'candacecansler@gmail.com']
                subject = 'Website Comment - ManagementSolutions'
                message = 'Name: '+ first + '\ncompany: ' + company + '\nComments: '+ comment +'\nEmail:  ' + email2

                try:
                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = ", ".join(send_to_email)
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    return render(request, 'thankyou.html')
                except:
                    return HttpResponse("Whoops, email did not send.  Please email us directly ot try again.")

            else:
                return HttpResponse("Whoops, emails did not match")

    return render(request, 'contact.html')




def services(request):
        return render(request, 'services.html')

def thankyou(request):
        return render(request, 'thankyou.html')
