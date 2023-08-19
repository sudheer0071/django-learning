from django.shortcuts import render
from django.http import HttpResponse
# from .models import Post
 
# Create your views here

posts  = [
    {
        'author': 'Dummy1',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'August 27 2018'
    },
    {
        'author': 'Dummy2',
        'title': 'Blog Post 2',
        'content':'second post content',
        'date_posted': 'August 28 2018'
    },
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

# def about(request):
#     return HttpResponse('<h1>this is about</h1>')
 
def about(request):
    return render(request,'blog/about.html', {'title': 'About'}) 