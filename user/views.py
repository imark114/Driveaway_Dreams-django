from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm,ChangeUserData
from django.views.generic import CreateView, TemplateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from car.models import SoldCar
# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request,'Account Created Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Sign Up'
        return context
    
class UserLoginView(LoginView):
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged In Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Given informations are incorrect')
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs) -> dict[str]:
            context = super().get_context_data(**kwargs)
            context["type"] = 'Login'
            return context
        

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def profile(request):
    cars = SoldCar.objects.filter(buyer=request.user)
    return render(request,'profile.html', {'cars': cars})

@login_required          
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = ChangeUserData(instance=request.user)
        return render(request,'form.html', {'form': profile_form,'type':'Update'})

# @login_required
# def pass_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user= request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Password Updated Successfully')
#             update_session_auth_hash(request,form.user)
#             return redirect('profile')
#     form = PasswordChangeForm(user=request.user)
#     return render(request,'form.html',{'form':form,'type': 'Change Password'})

@method_decorator(login_required,name='dispatch')
class PassChangeView(PasswordChangeView):
    template_name = 'form.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Change Password'
        return context
    
    