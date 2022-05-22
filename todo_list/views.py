from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def home(request):
    form = ListForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has been added to list!'))
            context = {
                'all_items':all_items,
                'form':form,
            }
            return redirect('home')
            # return render(request,'home.html',context)
    else:

        all_items = List.objects.all
        context = {
            'all_items':all_items,
            'form':form,

        }
        redirect('home')

    return render(request,'home.html',context)


def update(request, list_id):
    item = get_object_or_404(List, id=list_id)
    # item = List.objects.get(pk=list_id)
    all_items = List.objects.all

    form = ListForm(instance=item)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            # messages.success(request,('Item has been added to list!'))
            return redirect("home")
    context = {
        'form' : form,
        'all_items':all_items,
        
    }
            
    return render(request, "home.html", context)

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been deleted!'))
    return redirect('home')

def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')