from django.shortcuts import render, HttpResponse
from myapp.models import hel
from django.contrib.messages import get_messages
# Create your views here.

def index(request):
    return HttpResponse("hello everyone i am sahil verma")
def self(request):
    return HttpResponse("I am sahil verma and i have done my 12th from hbse board with 95%")
def name(request):
    return HttpResponse("s_a_h_i_l  v_e_r_m_a")
def contact(request):
    print("hiiii: ",request.POST.get("name"))
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        sahil=hel(name=name, email=email, password=password)
        sahil.save()

    return render(request, 'contact.html')
def save(request):
    return render(request, 'contact.html')
    # return HttpResponse("8198989299, sv7563999@gmail.com")
def verma(request):
    context={ 'variable': 100}
    return render(request, 'verma.html',context)
