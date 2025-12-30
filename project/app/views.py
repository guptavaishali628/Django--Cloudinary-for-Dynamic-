from django.shortcuts import render
from .models import Student

# Create your views here.
def index(req):
    return render(req,'index.html')

def register(req):
    if req.method=='POST':
        image=req.POST.get('image')
        video=req.POST.get('video')
        audio=req.POST.get('audio')
        file=req.POST.get('file')
        Student.objects.create(Image=image, Video=video, Audio=audio, File=file).save()
        return render(req,'show_data.html')

def show_data(req):
    data=Student.objects.all()
    return render(req,'show_data.html', {'data':data})   
    




