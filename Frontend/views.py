from django.contrib import messages
from django.shortcuts import render,redirect
from Backent.models import categorydb,productdb,contactdb
from Frontend.models import customerdb, cartdb,checkoutdb,wishlistdb
from django.db.models import query
from django.http import HttpResponse 
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404



# Create your views here.

def homepage(req):
    data = categorydb.objects.all()
    return render(req, "home.html", {'data': data})


def contactpage(req):
    return render(req,"contact.html")


def categorypage(req):
    data = categorydb.objects.all()
    return render(req,"categories.html",{'data': data})


def disproduct(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(Category=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"product.html",context)

def productsingle(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'dat':data})

def savecontactus(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        sb = req.POST.get('subject')
        ms = req.POST.get('message')
        obj = contactdb(Name=na,Email=em,Subject=sb,Message=ms)
        obj.save()
        messages.success(req, "Message sent")

        return redirect(contactpage)

def weblogin(req):
    return render(req,"weblogin.html")

def savecustomer(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        Em = request.POST.get('email')
        pas = request.POST.get('password')
        Cp  = request.POST.get("conpassword")
        if pas==Cp:
            obj = customerdb(Username=Us,Password=pas,Confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request, "Registered Successfully")

        return redirect(weblogin)
    

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if customerdb.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request, "Login Successfully...!")
            return redirect(homepage)
        else:
            messages.error(request,"Invalid User..!")
            return render(request,'weblogin.html')
        

# def custemerlogin(request):
#     if request.method == 'POST':
#         Username_r = request.POST.get("username")
#         Password_r = request.POST.get("password")

#         if customerdb.objects.filter(Username=Username_r, Password=Password_r).exists():
#             # Retrieve user from the database
#             user = customerdb.objects.get(Username=Username_r, Password=Password_r)

#             # Set the user_id in the session
#             request.session['user_id'] = user.id

#             messages.success(request, "Login Successfully...!")
#             return redirect(homepage)
#         else:
#             messages.error(request, "Invalid User..!")
#             return render(request, 'weblogin.html')



def some_protected_view(request):
    username = request.session['username']
    return render(request, 'weblogin.html', {'username': username})

def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    request.session.flush()
    return redirect(weblogin)

def savecart(req):
    if req.method=="POST":
        pna = req.POST.get('prodname')
        cat = req.POST.get('procart')
        qty= req.POST.get('quantity')
        tprice = req.POST.get('totalprice')
        obj = cartdb(Proname=pna,Category=cat,Quantity=qty,Price=tprice)
        obj.save()
        messages.success(req, "Added to Cart")
        return redirect(homepage)
    
def viewcartpage(req):
    data = cartdb.objects.all()
    return render(req,"addcart.html",{'data':data})

def deletecartfont(req,dataid):
    data = cartdb.objects.get(id=dataid)
    data.delete()
    return redirect(viewcartpage)

def check(req):
    data = cartdb.objects.all()
    return render(req,"checkout.html",{'data':data})

def savecheck(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        add= req.POST.get('address')
        pi = req.POST.get('pincode')
        ph = req.POST.get('phone')
        py= req.POST.get('cname')

        pa = req.POST.get('prodname')
        obj = checkoutdb(Name=na,Email=em,Address=add,Pincode=pi,Phone=ph,CardName=py,Expiration=pa)
        obj.save()
        messages.success(req, "Your order has been placed")

        return redirect(homepage)
 
def search_results(request):
    query = request.GET.get('query', '')
    
    
    results = productdb.objects.filter(Name__icontains=query)
    
    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search.html', context)


def wishlist(request):
 
    user_id = request.user.id
    wishlist_items = wishlistdb.objects.filter(Customer_id=user_id)
    

    # Print some information for debugging
    print("User ID:", user_id)
    print("Wishlist Items:", wishlist_items)

    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def add_to_wishlist(request, product_id):
    user_id = request.user.id
    
    
    if user_id is not None:
        product = get_object_or_404(productdb, id=product_id)

        if not wishlistdb.objects.filter(Customer_id=user_id, Product=product).exists():
            wishlist_item = wishlistdb(
                Customer_id=user_id,
                Product=product,
                ProductName=product.product_name,  # Assuming your wishlistdb model has a field 'ProductName'
                ProductImage=product.product_image,  # Assuming your wishlistdb model has a field 'ProductImage'
            )
            wishlist_item.save()
            messages.success(request, "Added to Wishlist")
        else:
            messages.warning(request, "Product is already in the Wishlist")

        return redirect('product_detail', product_id=product_id)
    else:
        messages.warning(request, "You need to be logged in to add to the wishlist")
        return redirect('weblogin')

def remove_from_wishlist(request, wishlist_id):
    user_id = request.user.id  # Use request.user.id to get the user object, assuming the user is authenticated
    wishlist_item = get_object_or_404(wishlistdb, Customer_id=user_id, id=wishlist_id)
    wishlist_item.delete()
    messages.success(request, "Removed from Wishlist")
    return redirect('wishlist')

