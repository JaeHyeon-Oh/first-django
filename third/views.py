from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestaurantForm



def list(request):
    restaurants=Restaurant.objects.all()
    paginator=Paginator(restaurants,5)

    page=request.GET.get('page')
    items=paginator.get_page(page)

    context={
        'restaurants': items
    }

    return render(request,'third/list.html',context)

def create(request):
    if request.method=='POST':
        form=RestaurantForm(request.POST)
        if form.is_valid():
            new_item=form.save()
        return redirect('/third/list/')
    form=RestaurantForm()
    return render(request,'third/create.html',{'form':form})

def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)  # NOTE: instance 인자(수정대상) 지정
        if form.is_valid():
            item = form.save()
    elif 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})

    return redirect('/third/list/')  # 리스트 화면으로 이동합니다

def detail(request):
    if 'id' in request.GET:
        item=get_object_or_404(Restaurant,pk=request.GET.get('id'))
        return render(request,'third/detail.html',{'item':item})
    return redirect('/third/list/')

def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return redirect('/third/list/')