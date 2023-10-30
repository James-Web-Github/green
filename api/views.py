from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def returnurl(request):
    print(request)
    
def clienturl(request):
    return render(request,'clientback.html')