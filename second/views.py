from django.shortcuts import render,redirect
from second.models import Post
from .form import PostForm

def list(request):
    context={
        'items':Post.objects.all()
    }
    return render(request,'second/list.html',context)

def create(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            new_item=form.save()
        return redirect('/second/list/')
    form=PostForm()
    return render(request,'second/create.html',{'form':form})

def confirm(request):
    form=PostForm(request.POST)
    if form.is_valid():
        return render(request,'second/confirm.html',{'form':form})
    return redirect('second/create/')