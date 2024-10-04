from django.shortcuts import render

def home(request):
    context = {}
    return render(request=request, template_name='home.html', context=context)