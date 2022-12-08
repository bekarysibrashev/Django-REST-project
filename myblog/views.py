from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.views import View
from .models import Post, Test
from django.core.paginator import Paginator
from .forms import SigUpForm, SignInForm, FeedbackForm, PostCreateForm
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponseRedirect 
from django.core.mail import send_mail, BadHeaderError

class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if paginator.count > 3:
            return render(request, 'myblog/home.html', context={
                'page_obj': page_obj
            })
        else:
            return render(request, 'myblog/home.html', context={
                'page_obj': posts
            })


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        try:
            all_posts = Post.objects.all()[:3]
            post = Post.objects.get(url=slug)
        except Post.DoesNotExist:
            raise Http404
        return render(request, 'myblog/post_detail.html', context={
            'post': post, 'all': all_posts
    })


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'myblog/signin.html', context={
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signin.html', context={'form':form})

    
class LogOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
    


class SearchView(View):
    def get(sekf, request):
        return render(request, 'myblog/search.html', context={
            'title': "Поиск"
        })



class FeedbackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'myblog/contactus.html', context={
            'form' : form,
            'title' : 'Написать мне'
        })

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(f'From {name} | {subject}', message, from_email, ['beka.ibrashev@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            
            return HttpResponseRedirect('success')
        return render(request, 'myblog/contactus.html', context={'  form':form})

        

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/success.html', context={
            'title': 'Спасибо'
        })

    
class PostCreateView(View):
    def get(self, request):
        form = PostCreateForm()
        return render(request, 'myblog/create_post.html', context={'form':form})

    def post(self, request):
        form = PostCreateForm(request.POST, request.FILES   )
        if form.is_valid():
            form.save()
            
        else:
            return HttpResponse('Не правильно')
        return render(request, 'myblog/success.html')