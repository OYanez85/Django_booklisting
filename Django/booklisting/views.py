from django.shortcuts import render

# Create your views here.
def booklisting(request):
    return render(request, 'booklisting.html', {})