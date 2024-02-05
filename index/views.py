from django.shortcuts import render, redirect
from posts.models import *
from django.shortcuts import render, get_object_or_404
from index.models import Baner
from posts.models import Post
from users.forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        main_categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
        # categories = Category.objects.filter(subcategories__isnull=True).prefetch_related('subcategories')
        categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
        context = {
            'categories': categories,
            'baners': Baner.objects.all(),
            'main_categories': main_categories
        }
        
        return render(request, 'index/index.html', context)
    
    else:
        return redirect('login')



def list_categories(request, cat_id):
    if request.user.is_authenticated:
        # Получаем родительскую категорию
        parent_category = get_object_or_404(Category, id=cat_id)

        # Получаем подкатегории родительской категории
        subcategories = parent_category.subcategories.all()


        context = {
            'parent_category': parent_category,
            'subcategories': subcategories,
        }
        
        return render(request, 'index/list_categories.html', context)
    else:
        return redirect('login')


def sub_list_categories(request, cat_id):
    if request.user.is_authenticated:
        # Получаем родительскую категорию
        parent_category = get_object_or_404(Category, id=cat_id)

        # Получаем подкатегории родительской категории
        subcategories = parent_category.subcategories.all()


        context = {
            'parent_category': parent_category,
            'subcategories': subcategories,
        }
        
        return render(request, 'index/sub_list_categories.html', context)
    else:
        return redirect('login')

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    back_url = request.META.get('HTTP_REFERER')  # Получение URL предыдущей страницы
    context = {'post': post,'back_url': back_url}
    return render(request, 'index/post.html', context=context)

def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse_lazy('index')

    redirect_authenticated_user = True