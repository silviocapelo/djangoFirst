from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormName, ModeFormClient


# Create your views here.

def index(request):
    a = 3
    b = 4
    soma = a + b
    return render(request, 'mytemplate/index.html', {'soma': soma})


def create(request):
    a = 50
    b = 50
    soma = a + b
    return render(request, 'mytemplate/help.html', {'soma': soma})


def sp(request):
    return render(request, 'index2.html')


def calc(request):
    return render(request, 'index.html')


def template(request):
    return render(request, 'template.html')


def form(request):
    form2 = ModeFormClient(request.POST)

    if request.method == 'POST':
        form2 = ModeFormClient(request.POST)
        if form2.is_valid():
            print("Os campos estão corretos")
            print("Name" + form2.cleaned_data['name'])
            print("Email" + form2.cleaned_data['email'])
            print("Texto" + form2.cleaned_data['observacao'])
            form2.save(commit=True)
        else:
            print("Erro")
    return render(request, 'form.html', {'form': form2})


def form_name(request):
    form = FormName(request.POST)
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print("Os campos estão corretos")
            print("Name" + form.cleaned_data['name'])
            print("Email" + form.cleaned_data['email'])
            print("Texto" + form.cleaned_data['observacao'])
    return render(request, 'form2.html', {'form': form})

