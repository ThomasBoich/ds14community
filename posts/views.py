from django.shortcuts import render

# Create your views here.





from django.shortcuts import render, redirect
from .forms import PostForm, CategoryForm
from .models import CustomUser

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})



def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'posts/category_edit.html', {'form': form})