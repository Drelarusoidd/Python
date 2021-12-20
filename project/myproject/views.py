from django.shortcuts import render
from .forms import  CustomersForm
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse

def attached(interior, logo, graphic):
    htmlcontent = ''
    if interior == 'true' and logo == 'true' and graphic == 'true':
        with open('myproject\static\\attachments\emailattach.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif interior == 'true':
        with open('myproject\static\\attachments\\attachInterior.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif logo == 'true':
        with open('myproject\static\\attachments\\attachLogo.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif graphic == 'true':
        with open('myproject\static\\attachments\\attachGraphic.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif interior == 'true' and graphic == 'true':
        with open('myproject\static\\attachments\\attachGraphicInterior.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif graphic == 'true' and logo == 'true':
        with open('myproject\static\\attachments\\attachGraphicInterior.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif interior == 'true' and logo == 'true':
        with open('myproject\static\\attachments\\attachLogoInterior.html', 'r') as file:
            htmlcontent = file.read()
        return htmlcontent
    elif interior == 'false' and logo == 'false' and graphic == 'false':
        return htmlcontent

def contacts(request):

    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        interior = request.POST['interior']
        logo = request.POST['logo']
        graphic = request.POST['graphic']

        htmlcontent = attached(interior, logo, graphic)
        msg = EmailMultiAlternatives('Examples work',
            f'From Sokol Design Company.\nGood day {name}.\n',
          'buble.1205@gmail.com',
           [f'{email}'],
           reply_to=['buble.1205@gmail.com'],
        )

        if htmlcontent != '':
            form = CustomersForm(request.POST)
            if form.is_valid(): form.save()
            msg.attach_alternative(htmlcontent, 'text/html')
            msg.send(fail_silently=False)
            return JsonResponse({'result': name,})
        else:
            return JsonResponse({'result': 'error'}, status=500)
    else:
        return render(request, 'myproject\contacts.html')

def myhome(request):
    return render(request, 'myproject\home.html')

def design(request):
    return render(request, 'myproject\designs.html')
