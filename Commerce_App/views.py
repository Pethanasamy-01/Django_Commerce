from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import CustomUserModel,Product,Wishlist
from .forms import RegisterForm,LoginForm,ProductForm,OrderForm
from django.contrib.auth import login,logout,authenticate
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from django.urls import reverse_lazy


# Create your views here.


def home(request): 
    return render(request,'home.html',{'user':request.user.username})

def register(request):
    if request.user.is_authenticated:
       return redirect('Home')
    if request.method=='POST':
      form=RegisterForm(request.POST)
      if form.is_valid():
          user=form.save()
          user.set_password(form.cleaned_data['password'])
         
          user.is_staff=True
          user.is_superuser=True
          user.save()
          login(request,user)
          return redirect ("Home")
      else:
         messages.error(request,'Check Password or Email. !!!')
         return redirect('Register')  
    else:        
      form=RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.user.is_authenticated:
       return redirect('Home')
    if request.method=='POST':
       form=LoginForm(request.POST)
       if form.is_valid():
          email=form.cleaned_data['email']
          password=form.cleaned_data['password']
          remember_me=form.cleaned_data['remember_me']

          if remember_me:
              request.session.set_expiry(60 * 60 *24 *30)              
          else:
              request.session.set_expiry(0)

          user=authenticate(email=email,password=password)
          if user is not None:
             login(request,user)
             return redirect('Home')   
          else:
               messages.error(request,'Check Password or Email. !!!')   
    else:           
     form=LoginForm()
    return render(request,'login.html',{'form':form})


class AllProducts(ListView):
   model=Product
   template_name='all_products.html'
   context_object_name='products' 
   paginate_by=4
   ordering=['id']

class CreateProduct(CreateView):
   model=Product
   template_name='product_create.html' 
   form_class=ProductForm
   success_url=reverse_lazy('All_Products')
   

def wishlist_product(request,id):
   product=get_object_or_404(Product,id=id)

   wishlist,created=Wishlist.objects.get_or_create(user=request.user)

   if product not in wishlist.products.all():
      wishlist.products.add(product)
   return redirect('Wishlist_View')
     
def wishlist_view(request):

   wishlist=Wishlist.objects.filter(user=request.user) .first()

   if wishlist:
      products=wishlist.products.all()
   else:
      products=[]       

   return render(request,'wishlist.html',{'products':products})   

def wishlist_remove(request,id):
   product=get_object_or_404(Product,id=id)

   wishlist=Wishlist.objects.filter(user=request.user).first()

   if wishlist and product in wishlist.products.all():
      wishlist.products.remove(product)

   return redirect('Wishlist_View')   

def user_profile(request):
   return render(request,'user_profile.html',{'name':request.user.username})


class Product_Detail(DetailView):
   model=Product
   template_name='product_detail.html'
   context_object_name= 'products'
     
def order(request,pk):  
   if pk:
      product=Product.objects.get(id=pk)
   form=OrderForm()
   return render(request,'order.html',{'form':form,'price':product.price})


def logout_view(request):
   logout(request)
   return redirect('Home')

