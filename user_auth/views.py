from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.
def user_login(request):
    """
    Renders the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login page.
    """
    return render(request, 'authentication/login.html')

class CustomLoginView(LoginView):
    """
    Custom login view that redirects authenticated users to a specific URL.
    """
    redirect_authenticated_user = True

def authenticate_user(request):
        """
    Authenticates a user based on POST data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the appropriate URL.
    """
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            return HttpResponseRedirect(
            reverse('user_auth:login')
            )
        else:
            login(request, user)
            return HttpResponseRedirect(
            reverse('user_auth:show_user')
            )

def show_user(request):
    """
    Renders the user's profile page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered user profile page.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register_user(request):
    """
    Renders the user registration page and handles form submission.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration page or a redirect to the login page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
