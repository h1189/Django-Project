from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import WebAppUser
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File



def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('files_list')
            
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('sign_in')

    else:
        return render(request,'sign_in.html')

   


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1'] 
        re_pass = request.POST['re_pass']
        if username == False:
            messages.info(request,'Username Required')

        if password == re_pass:
            if WebAppUser.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect("sign_up")
            elif WebAppUser.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect("sign_up")
            else:
                user = WebAppUser.objects.create_user(username = username, email = email, password = password)
                user.save(); 
                messages.info(request,"User Created")
                return redirect("sign_in")

        else:
            messages.info(request, 'Password not matched..')
            return redirect("sign_up")
    else:
        return render(request, 'sign_up.html')


def files_list(request):
    files = File.objects.all()
    return render(request,'files_list.html',{
        'files':files
    })

def file_upload(request):
    if request.method == 'POST':    
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files_list')
    else:
        form = FileForm()
    return render(request,'file_upload.html',{
        'form':form
    })
def home(request):
    file_count = File.objects.all().count()
    messages.info(request,file_count)
    return render(request,'home.html')