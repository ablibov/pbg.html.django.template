from django.shortcuts import render, redirect, get_object_or_404
from core.forms import RegisterForm
from core.models import User


def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:success')
    else:
        form = RegisterForm()

    return render(request, 'index.html', {'form': form})


def users(request):
    users = User.objects.order_by('-id')
    return render(request, 'users.html', {'users': users})

def detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'detail.html', {'user': user})

def success(request):
    return render(request, 'success.html')

def approve(request, id):
    user = get_object_or_404(User, id=id)
    user.status = "Accepted"
    user.save()
    return redirect('core:users')

def decline(request, id):
    user = get_object_or_404(User, id=id)
    user.status = "Declined"
    user.save()
    return redirect('core:users')

def moderation(request, id):
    user = get_object_or_404(User, id=id)
    user.admin = "Admin"
    user.save()
    return redirect('core:users')

def make_user(request, id):
    user = get_object_or_404(User, id=id)
    user.admin = "User"
    user.save()
    return redirect('core:users')