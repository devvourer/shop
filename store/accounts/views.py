from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, UserEditForm, ProfileEditForm
from django.core.mail import send_mail
from store import settings
from .models import User, Profile
from django.contrib.auth import logout

from django.http import HttpResponse
from django.contrib.auth import views, login, authenticate


def create_user(request, post_code=None):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.generate_activation_code()
            code = user.activation_code
            send_mail('Verification', f'Confirm your account with this activation code: {code}',
                      settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
            return redirect('accounts:verify')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', locals())


def verify(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            user = User.objects.get(activation_code=code)
            user.is_active = True
            Profile.objects.create(user=user)
            user.save()
            return redirect('accounts:login')
        except ObjectDoesNotExist:
            return HttpResponse('Code is invalid')
    return render(request, 'accounts/verify.html')


def user_login(request):
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:product_list')
                else:
                    return HttpResponse('Disabled account')
        except ObjectDoesNotExist:
            return HttpResponse('Account not found')
    # else:
    #     form = LoginForm()
    return render(request, 'accounts/login.html', locals())


def logout_view(request):
    logout(request)
    return redirect('shop:product_list')



@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'accounts/edit.html', locals())





