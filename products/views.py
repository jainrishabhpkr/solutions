from django.shortcuts import render , get_object_or_404, redirect
from products.models import Product
from products.forms import ProductForm

# Create your views here.




def listview(request):
    list = Product.objects.all()
    mydict = {'product_list':list}
    return render(request,'products/product_list.html',context=mydict)

def productdetailview(request, slug):
    product = get_object_or_404(Product, slug = slug)
    mydict={'product':product}
    return render(request,'products/product_detail.html',context=mydict)


def productaddview(request):
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()

    return render(request,'products/form.html',{'form':form})

def successview(request):
    return render(request,'products/success.html')

def homeview(request):
    return render(request,'products/home.html')
