from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import DoubanTop250
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from .models import DoubanTop250, Comment, Name, User
from .models import AuthUser

def search(request):
    context = {'user': request.user}

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

        elif search_mode == 'actors' and search_query:
            # 演员搜索逻辑
            names = Name.objects.filter(primaryname__icontains=search_query)
            name_data = []
            for name in names:
                known_for_titles = name.knownfortitles.split(',') if name.knownfortitles else []
                titles_info = DoubanTop250.objects.filter(tconst__in=known_for_titles).values_list('primarytitle',
                                                                                                   flat=True)
                name_info = {
                    'primaryName': name.primaryname,
                    'birthYear': name.birthyear,
                    'deathYear': name.deathyear,
                    'primaryProfession': name.primaryprofession,
                    'knownForTitles': titles_info
                }
                name_data.append(name_info)
            context['name_data'] = name_data

    return render(request, 'titles/search.html', context)


def submit_review(request):
    if request.method == 'POST':
        tconst = request.POST.get('tconst')
        userid = request.user.id  # 获取当前登录用户的ID
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        # 存储评价数据
        new_comment = Comment(tconst=tconst, userid=userid, rating=rating, comment=comment)
        new_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    # 如果不是POST请求，重定向回首页或其他页面
    return HttpResponseRedirect('/index/')


def title_info(request, title):
    context = {}
    movie = DoubanTop250.objects.filter(primarytitle=title).first()  # 获取电影对象
    comments = Comment.objects.filter(tconst=movie.tconst)  # 获取评论对象

    context['movie'] = movie
    context['comments'] = comments

    return render(request, 'titles/title_info.html', context)


def administrator_show(request):
    users = AuthUser.objects.all()
    return render(request, 'administrator/administrator.html', {'users': users})


def get_mark(request, user_id):
    # 获取用户的标记信息
    user_comments = Comment.objects.filter(userid=user_id).values('tconst', 'comment', 'rating', 'commentid')

    # 获取每个评论对应的 primaryTitle
    for comment in user_comments:
        tconst_value = comment['tconst']
        primary_title = DoubanTop250.objects.get(tconst=tconst_value).primarytitle
        url = DoubanTop250.objects.get(tconst=tconst_value).urls
        comment['primaryTitle'] = primary_title
        comment['url'] = url

    # 将查询结果传递给模板
    context = {
        'user_comments': user_comments,
    }
    return render(request, 'mark/mark.html', context)

@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, commentid=comment_id)
    comment.delete()
    return redirect('get_mark', user_id=comment.userid)

def delete_user(request, user_id):
    user = get_object_or_404(AuthUser, id=user_id)
    user.delete()
    return redirect('administrator')  # 重定向到管理用户信息的页面