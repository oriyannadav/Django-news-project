from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        # Save the user object from the form
        user = form.save()

        # Check for form validation errors
        if form.errors:
            print(form.errors)

        # Return the super class's form_valid method
        return super().form_valid(form)


class ChangeAccountView(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'users/changeAccount.html'

    def form_valid(self, form):
        # Save the user object from the form
        user = form.save()

        # Get the bio and profile_picture from the form's cleaned data
        bio = form.cleaned_data.get('bio')
        profile_picture = form.cleaned_data.get('profile_picture')

        # Create the user profile with the bio and profile_picture
        UserProfile.objects.create(user=user, bio=bio, profile_picture=profile_picture)

        # Return the super class's form_valid method
        return super().form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                        "if an account exists with the email you entered. You should receive them shortly." \
                        " If you don't receive an email, " \
                        "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/createAccount.html', {'form': form})

@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form, 'user_profile': user_profile})


@login_required
def change_account_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/change_account.html')