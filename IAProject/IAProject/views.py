from django.shortcuts import render

def landingView(request):
    template_name = "landingpage.html"
    context = {}
    return render(request,template_name,context)