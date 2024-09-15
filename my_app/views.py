from django.shortcuts import render, redirect
from .models import Shoe, Lace
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def about(request):
  return render(request, 'about.html')

@login_required
def shoe_index(request):
  shoes = Shoe.objects.filter(user=request.user)
  return render(request, 'shoes/index.html', {'shoes': shoes})

@login_required
def shoe_detail(request, shoe_id):
  shoe=Shoe.objects.get(id=shoe_id)
  laces_shoe_doesnt_have = Lace.objects.exclude(id__in = shoe.laces.all().values_list('id'))
  return render(request, 'shoes/detail.html', {'shoe': shoe, 'laces': laces_shoe_doesnt_have,})

@login_required
def associate_lace(request, shoe_id, lace_id):
  Shoe.objects.get(id=shoe_id).laces.add(lace_id)
  return redirect('shoe_detail', shoe_id = shoe_id)

@login_required
def disassociate_lace(request, shoe_id, lace_id):
  Shoe.objects.get(id=shoe_id).laces.remove(lace_id)
  return redirect('shoe_detail', shoe_id = shoe_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shoe_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView, LoginRequiredMixin):
  template_name = 'home.html'

class ShoeCreate(CreateView, LoginRequiredMixin):
  model = Shoe
  fields = ['model', 'brand', 'purchase_date', 'size', 'price', 'description', 'current_condition', 'photo' ]
  # success_url = '/shoes/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class ShoeUpdate(UpdateView, LoginRequiredMixin):
  model = Shoe
  fields = ['model', 'brand', 'purchase_date', 'size', 'price', 'description', 'current_condition', 'photo' ]
  
class ShoeDelete(DeleteView, LoginRequiredMixin):
  model = Shoe
  success_url = '/shoes/'

class LaceCreate(CreateView, LoginRequiredMixin):
  model = Lace
  fields = '__all__'
  
class LaceDetail(DetailView, LoginRequiredMixin):
  model = Lace
  
class LaceList (ListView, LoginRequiredMixin):
  model = Lace
  
class LaceUpdate (UpdateView, LoginRequiredMixin):
  model = Lace
  fields = 'color'

class LaceDelete (DeleteView, LoginRequiredMixin):
  model = Lace
  success_url = '/laces/'