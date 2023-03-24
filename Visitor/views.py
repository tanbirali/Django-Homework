from django.shortcuts import render

from .models import Visitor
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        visitor = Visitor(name=name)
        visitor.save()
    return render(request,'index.html')


def visitors(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors.html', {'visitors': visitors})




