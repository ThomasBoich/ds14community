from django.shortcuts import render

# Create your views here.





from django.shortcuts import render, redirect
from .forms import PostForm
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
