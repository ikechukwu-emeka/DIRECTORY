from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Telephone
from django.urls import reverse
from django.contrib import messages
from .forms import TelephoneForm



def homepage(request):
    context = {
        'record': Telephone.objects.all()
    }
    return render(request, 'telephone/index.html', context)


def insert(request):
    form = TelephoneForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    return render(request, 'telephone/add.html', context)


def cancel_record(request, id):
    record = Telephone.objects.get(id=id)
    record.delete()
    messages.success(request, 'record deleted')
    return redirect(reverse('index'))


def alter_record(request, id):
    record = Telephone.objects.get(id=id)
    form = TelephoneForm(request.POST or None,
                         request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'telephone/alter.html', context)

