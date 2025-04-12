from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def page3(request):
    return render(request, 'page3.html')

