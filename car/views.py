from django.shortcuts import render,redirect
from django.views.generic import DetailView, FormView
from .models import Car, Comment, SoldCar
from .forms import CommentForm
# Create your views here.
class carDetailsView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def BuyCar(request, id):
    car = Car.objects.get(pk=id)
    car.quantity -=1
    newSold = SoldCar()
    newSold.buyer = request.user
    newSold.car = car
    newSold.save()
    car.save()
    return redirect('home')