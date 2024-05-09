# details/views.py
from django.shortcuts import render, redirect
from .forms import DetailForm
from .models import Detail

def add_detail(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_list')
    else:
        form = DetailForm()
    return render(request, 'details/add_detail.html', {'form': form})

def detail_list(request):
    details = Detail.objects.all()
    return render(request, 'details/detail_list.html', {'details': details})

