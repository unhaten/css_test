from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html',)

def testroom(request):
    return render(request, 'testroom.html')
