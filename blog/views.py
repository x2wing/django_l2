from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_t(request):
    """ получение данных с формы"""
    # если поле http method== "POST"
    if request.method == "POST":
        # получаем данные с формы
        form = PostForm(request.POST)
        # вытаскиваем данные из ответа сервера
        title = int(form.data['title'])
        data1 = int(form.data['data1'])
        data2 = int(form.data['data2'])
        # вывод данных на форму
        return render(request, 'blog/out.html', {'title': title,
                                                 'data1': data1,
                                                 'data2': data2,})
    # если первая загрузка формы
    else:
        form = PostForm()
    # первая загрузка формы. render генерит html
    return render(request, 'blog/post_edit.html', {'form': form})
