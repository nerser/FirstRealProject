from django.shortcuts import render

# Create your views here.
def main_about(request):
    return render(request, 'about/about.html')