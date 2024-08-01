from django.core.paginator import Paginator
from django.shortcuts import render
from third.models import Restaurant
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect
# Create your views here.


def list(request):
    restaurant = Restaurant.objects.all()
    paginator = Paginator(restaurant, 5)

    page = request.GET.get('page') # third/list?page=1
    items = paginator.get_page(page)

    context = {
        "restaurants": items
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_items = form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form':form})


def update(request):
    if request.method == "POST" and 'id' in request.POST:
        item = Restaurant.objects.get(pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        item = Restaurant.objects.get(pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')