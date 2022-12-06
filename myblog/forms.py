from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Post
from django.forms import ModelForm,  ClearableFileInput, TextInput, Textarea, URLInput, FileInput
from django.utils import timezone

class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputUsername'
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )








class SigUpForm(forms.Form):
    
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth




class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['h1','title','url', 'description', 'content', 'tag', 'image']
# , 'h1', 'description', 'content', 'image', 'tag'




# '''Для того чтобы форма сработала нам нужно заполнить ее правильно 
#     То есть 1) проверить на наличие ошибки.(Который из полей не подходит для заполнения )
#     То есть 2) Попробовать удалить РИЧ ТЕКСТ настройки в сеттинге для контетн поля
#     То есть 3) Проверить УРЛ поля. '''

    widgets = {
        'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'title'
        }),
        'h1': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'h1'
        }),
        'url': URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'url'
        }),
        'description': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'description'
        }),
        'content': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'content'
        }),
        'image': ClearableFileInput(attrs={
            'class': 'form-control',
            'placeholder': 'image'
        }),
        'tag': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'tag'
        })
    }








class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id' : 'name',
            'placeholder': "Ваше Имя"
        })
    )

    email = forms.CharField(
        max_length=200,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id' : 'email',
            'placeholder': "Ваша почта"
        })
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id' : 'subject',
            'placeholder': "Ваше сообщение"
            })
    )

    message = forms.CharField(
        widget = forms.Textarea(attrs={
            'class' : 'form-control',
            'id': 'message',
            'rows': 2,
            'placeholder': 'Ваше сообщение'
        })
    )