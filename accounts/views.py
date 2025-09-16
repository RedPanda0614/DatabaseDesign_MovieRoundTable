from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            login(request, user)
            return redirect('../login')  # 重定向到主页或其他页面
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../index/')  # 重定向到主页或其他页面
        else:
            messages.error(request, '用户名或密码不正确')

    return render(request, 'login.html')


from django.shortcuts import render
from .models import DoubanTop250, Comment, Name


def search(request):
    context = {}
    if request.method == 'POST':
        search_mode = request.POST.get('search_mode', 'movies')
        search_query = request.POST.get('query', None)

        if search_mode == 'movies' and search_query:
            # 电影搜索逻辑
            movies = DoubanTop250.objects.filter(primarytitle__icontains=search_query)
            movie_data = []
            for movie in movies:
                comments = Comment.objects.filter(tconst=movie.tconst)
                movie_data.append({
                    'movie': movie,
                    'comments': comments
                })
            context['movie_data'] = movie_data
            # return render(request, '../../app01/templates/titles/results.html', context)
            return redirect('search_movie')

        elif search_mode == 'actors' and search_query:
            # 演员搜索逻辑
            actors = Name.objects.filter(primaryname__icontains=search_query)
            context['actor_data'] = actors
            context = {
                'user': request.user
            }

    return render(request, 'index.html', context)


def administrator_login(request):
    if request.method == 'POST':
        username = request.POST['administrator_name']
        password = request.POST['administrator_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../administrator/')  # 重定向到管理员界面，需要修改
        else:
            messages.error(request, '用户名或密码不正确')

    return render(request, 'administrator_login.html')


def administrator_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            login(request, user)
            return redirect('../administrator_login/')  # 重定向到管理员登录
    else:
        form = UserRegistrationForm()
    return render(request, 'administrator_register.html', {'form': form})


def user_profile(request, user_id):  # 修改参数名为user_id
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user.html', {'user': user})


@login_required  # 仅允许已登录用户访问该视图
def update_user_info(request):
    if request.method == 'POST':
        # 处理表单提交
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')

        # 更新用户信息
        request.user.username = new_username
        request.user.email = new_email
        request.user.save()
        user_id = request.user.id

        # 重定向到用户信息页面或其他页面
        return redirect('user_profile', user_id=user_id)

    # 如果是 GET 请求，渲染包含表单的页面
    return render(request, 'update_user_info.html')