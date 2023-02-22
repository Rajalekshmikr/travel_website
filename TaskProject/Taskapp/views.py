from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import team

# Create your views here.
#def home(request):
    #return HttpResponse('<h2>hello welcome to happy cuppy cakes<h2><br>the number one cake server all over kerala thank you for trusting us')

#def about(request):
    #return render(request,'about.html' %}')
#def contact(request):
    #return render(request,'contact.html' %}')
#def details(request):
    #return HttpResponse('this is a detail page')
#def thanx(request):
     #return  render(request,'thanx.html' %}')
def demo(request):
        place_obj = place.objects.all()
        team_obj = team.objects.all()
        return render(request,'index.html',{'places':place_obj, 'teams':team_obj})
# def demo1(request):
#         tem=team.objects.all()
#         return render(request,'index.html',{'team':tem})
