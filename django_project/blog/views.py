from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts =[
  {
    'author':'COreyMs',
    'title' : 'Blog Post 2',
    'contect':'second post conent',
    'date_posed': 'Augest 27, 2018',
  },
  {
    'author':'Jane Doe',
    'title' : 'Blog Post 2',
    'contect':'second post conent',
    'date_posed': 'Augest 27, 2018',
  },

]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context,)

# def about(request):
#     return HttpResponse('<h1>this is about</h1>')

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})