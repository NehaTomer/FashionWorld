from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from Fashion.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay 

from .models import*
def indexpage(request):
    # request.session.flush()
    data=Product.objects.all().order_by("id")[0:15]
    product=Product.objects.all().order_by()[0:11]
    brands=Brand.objects.all()
    return render(request,"index.html",{'data':data,'product':product,'brands':brands})
def aboutpage(request):
    return render(request,"about.html")
def cartpage(request):
    return render(request,"cart.html")
def contactpage(request):
    if(request.method=="POST"):
        c=contact()
        c.name=request.POST.get("name")
        c.email=request.POST.get("email")
        c.phone=request.POST.get("phone")
        c.subject=request.POST.get("subject")
        c.message=request.POST.get("message")
        c.save()
        messages.success(request,"Thanks to share your query with us!!1Our team will contact you soon!!!")
    return render(request,"contact.html")
def productpage(request,mc,sc,br):
    if(mc=="All" and sc=="All" and br=="All"):
        data=Product.objects.all().order_by("-id")
    elif(mc!="All" and sc=="All" and br=="All"):
        data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
    elif(mc=="All" and sc!="All" and br=="All"):
        data=Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc=="All" and sc=="All" and br!="All"):
        data=Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-id")
    elif(mc!="All" and sc!="All" and br=="All"):
        data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc!="All" and sc=="All" and br!="All"):
        data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("-id")
    elif(mc!="All" and sc!="All" and br!="All"):
        data=Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    else:
        data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("-id")
       
    product=Product.objects.all().order_by()[0:11]
    maincategories=Maincategory.objects.all()
    subcategories=Subcategory.objects.all()
    brands=Brand.objects.all()
    return render(request,"product.html",{'data':data,'product':product,'maincategories':maincategories,'subcategories':subcategories,'brands':brands,'mc':mc,'sc':sc,'br':br})

def filterpage(request,mc,sc,br,filter):
    if(filter=='Latest'):
        if(mc=="All" and sc=="All" and br=="All"):
           data=Product.objects.all().order_by("-id")
        elif(mc!="All" and sc=="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
        elif(mc=="All" and sc!="All" and br=="All"):
           data=Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
        elif(mc=="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-id")
        elif(mc!="All" and sc!="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
        elif(mc!="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("-id")
        elif(mc!="All" and sc!="All" and br!="All"):
           data=Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
        else:
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("-id")
    elif(filter=="LTOH"):
        if(mc=="All" and sc=="All" and br=="All"):
           data=Product.objects.all().order_by("final_price")
        elif(mc!="All" and sc=="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("final_price")
        elif(mc=="All" and sc!="All" and br=="All"):
          data=Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("final_price")
        elif(mc=="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("final_price")
        elif(mc!="All" and sc!="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("final_price")
        elif(mc!="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("final_price")
        elif(mc!="All" and sc!="All" and br!="All"):
          data=Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("final_price")
        else:
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("final_price")
    else:
        if(mc=="All" and sc=="All" and br=="All"):
           data=Product.objects.all().order_by("-final_price")
        elif(mc!="All" and sc=="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-final_price")
        elif(mc=="All" and sc!="All" and br=="All"):
          data=Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-final_price")
        elif(mc=="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-final_price")
        elif(mc!="All" and sc!="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-final_price")
        elif(mc!="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("-final_price")
        elif(mc!="All" and sc!="All" and br!="All"):
          data=Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("-final_price")
        else:
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("-final_price")
    
    product=Product.objects.all().order_by()[0:9]
    maincategories=Maincategory.objects.all()
    subcategories=Subcategory.objects.all()
    brands=Brand.objects.all()
    return render(request,"product.html",{'data':data,'product':product,'maincategories':maincategories,'subcategories':subcategories,'brands':brands,'mc':mc,'sc':sc,'br':br,'filter':filter})

def PriceFilterPage(request,mc,sc,br):
    option=request.POST.get("price")
    min = 0
    max = 100000
    if(option=="1"):
        min = 0
        max = 100000
    elif(option=="2"):
        min = 0
        max = 1000
    elif(option=="3"):
        min = 1000
        max = 2000    
    elif(option=="4"):
        min = 2000
        max = 3000
    elif(option=="5"):
        min = 3000
        max = 4000      
    elif(option=="6"):
        min = 4000
        max = 5000
    elif(option=="7"):
        min = 5000
        max = 100000          

    if(mc=="All" and sc=="All" and br=="All"):
           data=Product.objects.filter(final_price__gte=min,final_price__lte=max).order_by("final_price")
    elif(mc!="All" and sc=="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),final_price__gte=min,final_price__lte=max).order_by("final_price")
    elif(mc=="All" and sc!="All" and br=="All"):
           data=Product.objects.filter(subcategory=Subcategory.objects.get(name=sc),final_price__gte=min,final_price__lte=max).order_by("final_price")
    elif(mc=="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(brand=Brand.objects.get(name=br),final_price__gte=min,final_price__lte=max).order_by("final_price")
    elif(mc!="All" and sc!="All" and br=="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),final_price__gte=min,final_price__lte=max).order_by("final_price")
    elif(mc!="All" and sc=="All" and br!="All"):
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br),final_price__gte=min,final_price__lte=max).order_by("final_price")
    elif(mc!="All" and sc!="All" and br!="All"):
           data=Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc),final_price__gte=min,final_price__lte=max).order_by("final_price")
    else:
           data=Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br),final_price__gte=min,final_price__lte=max).order_by("final_price")
    product=Product.objects.all().order_by()[0:9]
    maincategories=Maincategory.objects.all()
    subcategories=Subcategory.objects.all()
    brands=Brand.objects.all()
    return render(request,"product.html",{'data':data,'product':product,'maincategories':maincategories,'subcategories':subcategories,'brands':brands,'mc':mc,'sc':sc,'br':br,'filter':filter})


def searchpage(request):
    if(request.method=="POST"):
        search=request.POST.get("search")
        data=Product.objects.filter(Q(name__contains=search)|Q(color__contains=search)|Q(maincategory__name__contains=search)|Q(subcategory__name__contains=search))
        maincategories=Maincategory.objects.all()
        subcategories=Subcategory.objects.all()
        brands=Brand.objects.all()
        return render(request,"product.html",{'data':data,'maincategories':maincategories,'subcategories':subcategories,'brands':brands,'mc':'ALL','sc':'ALL','br':'ALL','filter':filter})

    else:
        return HttpResponseRedirect("/")

def testimonialpage(request):
    if(request.method=="POST"):
        t=testimonial()
        t.pic=request.POST.get("pic")
        t.name=request.POST.get("name")
        t.message=request.POST.get("message")
        t.save()
    data=testimonial.objects.all().order_by("id")
    return render(request,"testimonial.html",{'data':data})
def productdetailpage(request,num):
    data=Product.objects.get(id=num)
    product=Product.objects.filter(maincategory=Maincategory.objects.get(name=data.maincategory)).order_by()[0:7]
    return render(request,"product_details.html",{'data':data,'product':product})
def loginpage(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if(user is None):
            messages.error(request," Invalid username or password!!!")
        else:
            auth.login(request,user)
            if(user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
    return render(request,"login.html")

def signuppage(request):
    if(request.method=="POST"):
        if(request.POST.get("password")!=request.POST.get("cpassword")):
            messages.error(request,"password and confirm password doesn't matched")
        else:
            try:
                user=User.objects.create(username=request.POST.get("username"))
                user.set_password(request.POST.get("password"))
                user.save()
                

                b=Buyers()
                b.name=request.POST.get("name")
                b.username=request.POST.get("username")
                b.email=request.POST.get("email")
                b.phone=request.POST.get("phone")
                b.save()

                subject = 'Thanks to create an account:Team: FashionWorld'
                message = """
                      Hello """+b.name+"""
                      Thanks to create an account with us 
                      Now you can buy Latest Products
                     
                      Team: FashionWorld
                      """
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [b.email, ]
                send_mail( subject, message, email_from, recipient_list )
            
                return HttpResponseRedirect("/login/")
            except:
                messages.error(request,"username already taken!!!")
    return render(request,'signup.html')

def addtocartpage(request,num):
    p=Product.objects.get(id=num)
    if(p):
        cart=request.session.get("cart",None)
        if(cart):
            if(str(num) in cart):
                return HttpResponseRedirect("/cart/")
            else:
                cart.setdefault(str(num),{'id':p.id,'name':p.name,'brand':p.brand.name,'color':p.color,
                'price':p.final_price,'qty':1,'total':p.final_price,'pic':p.pic1.url})
        else:
            cart={str(num):{'id':p.id,'name':p.name,'brand':p.brand.name,'color':p.color,'price':p.final_price,'qty':1,'total':p.final_price,'pic':p.pic1.url}}
        subtotal=0
        count=0
        for key,values in cart.items():
            subtotal=subtotal+int(values['total'])
            count=count+values['qty']
        if(subtotal>0 and subtotal<1000):
            shipping=150
        else:
            shipping=0
        total=subtotal+shipping
        request.session["cart"]=cart
        request.session["subtotal"]=subtotal
        request.session["shipping"]=shipping
        request.session["total"]=total
        request.session["count"]=count
        request.session.set_expiry(60*60*24*30)
        return HttpResponseRedirect("/cart/")
    else:
        return HttpResponseRedirect("/product/All/All/All")

def cartpage(request):
    cart=request.session.get("cart",None)
    return render(request,'cart.html',{'cart':cart})

def removecartpage(request,num):
    cart=request.session.get("cart",None)
    
    if(cart and num in cart):
            del cart[num]
            request.session['cart']=cart
            subtotal=0
            count=0
            for key,values in cart.items():
              subtotal=subtotal+int(values['total'])
              count=count+values['qty']
            if(subtotal>0 and subtotal<1000):
                shipping=150
            else:
              shipping=0
            total=subtotal+shipping
            request.session["cart"]=cart
            request.session["subtotal"]=subtotal
            request.session["shipping"]=shipping
            request.session["total"]=total
            request.session["count"]=count
        
    return HttpResponseRedirect("/cart/")
   

def updatecartpage(request,num,op):
    cart=request.session.get("cart",None)
    if(cart and num in cart):
            item=cart[num]
            if(item['qty']==1 and op=='Dec'):
                return HttpResponseRedirect("/cart/")
            elif(op=='Dec'):
                item['qty']=item['qty']-1
                item['total']=int(item['total'])-int(item['price'])
            else:
                item['qty']=item['qty']+1
                item['total']= int(item['total'])+int(item['price'])
            request.session['cart']=cart
            subtotal=0
            count=0
            for key,values in cart.items():
              subtotal=subtotal+int(values['total'])
              count=count+values['qty']
            if(subtotal>0 and subtotal<1000):
                shipping=150
            else:
              shipping=0
            total=subtotal+shipping
            request.session["cart"]=cart
            request.session["subtotal"]=subtotal
            request.session["shipping"]=shipping
            request.session["total"]=total
            request.session["count"]=count
            request.session.set_expiry(60*60*24*30)
    return HttpResponseRedirect("/cart/")


@login_required(login_url="/login/")
def wishlistpage(request,num):
   try:
        p=Product.objects.get(id=num)
        buyer=Buyers.objects.get(username=request.user.username)
        try:
          wishlist=Wishlist.objects.get(buyer=buyer,product=p)
        except:
            w=Wishlist()
            w.buyer=buyer
            w.product=p
            w.save()
   except:
        pass
    
   return HttpResponseRedirect("/profile/")

def checkoutpage(request):
    try:
        buyer=Buyers.objects.get(username=request.user.username)
        return render(request,'checkout.html',{'buyer':buyer})
    except:
        return HttpResponseRedirect("/cart/")
    
client=razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
@login_required(login_url="/login/")
def placeorder(request):
    if(request.method=="POST"):
        buyer=Buyers.objects.get(username=request.user.username)
        mode=request.POST.get("mode")
        subtotal=request.session.get("subtotal",0)
        shipping=request.session.get("shipping",0)
        total=request.session.get("total",0)
        if(subtotal==0):
            return HttpResponseRedirect("/checkout/")
        check=Checkout()
        check.buyer=buyer
        check.subtotal=subtotal
        check.shipping=shipping
        check.final=total
        check.save()

        cart=request.session.get("cart",None)
        for key,values in cart.items():
            p=Product.objects.get(id=(int(key)))
            cp=CheckoutProducts()
            cp.checkout=check
            cp.product=p
            cp.qty=values['qty']
            cp.total=values['total']
            cp.save()
        request.session['cart']={}
        request.session['subtotal']=0
        request.session['shipping']=0
        request.session['total']=0
        request.session['count']=0
        if(mode=="COD"):
            subject = 'order has been placed: FashionWorld'
            message = """
                      Hello """+buyer.name+""""
                      your order has been placed
                      Team: FashionWorld
                      """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [buyer.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect("/confirmation/")
        
        else:
            orderAmount = check.final*100
            orderCurrency = "INR"
            paymentOrder = client.order.create(dict(amount=orderAmount,currency=orderCurrency,payment_capture=1))
            paymentId=paymentOrder["id"]
            check.paymentMode = 2
            check.paymentStatus=2
            check.save()      
            return render(request,"pay.html",{
                "amount":orderAmount,
                "api_key":RAZORPAY_API_KEY,
                "order_id":paymentId,
                "User":buyer,
                "checkid":9999999999
            }) 
    else:   
        return HttpResponseRedirect("/checkout/")
     
@login_required(login_url="/login/")    
def paymentSuccesspage(request,rppid,rpoid,rpsid,checkid):
        buyer = Buyers.objects.get(username = request.user)
        if(checkid==9999999999):
            check = Checkout.objects.filter(buyer=buyer)
            check=check[::-1]
            check=check[0]
        else:
            check = Checkout.objects.get(id=checkid)
            check.rppid=rppid
            check.paymentStatus=2
            check.save()

        subject = 'Order has been placed : Team FahionWorld'
        message = f"""Hi {buyer.name}, Your order  has been placed with order id {rppid}
                      kindly track you order in profile section 
                      Team:FahionWorld."""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [buyer.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponseRedirect("/confirmation/")
 


@login_required(login_url="/login/")    
def payAgainpage(request,checkid):
    try:
       buyer = Buyers.objects.get(username = request.user)
       check = Checkout.objects.get(id= checkid)
       orderAmount = check.final*100
       orderCurrency = "INR"
       paymentOrder = client.order.create(dict(amount=orderAmount,currency=orderCurrency,payment_capture=1))
       paymentId=paymentOrder["id"]
       check.paymentMode = 2
       
       check.save()      
       return render(request,"pay.html",{
           "amount":orderAmount,
           "api_key":RAZORPAY_API_KEY,
           "order_id":paymentId,
           "User":buyer,
           "checkid":checkid
               })    
    except:
        return HttpResponseRedirect("/profile/")


    
@login_required(login_url="/login/")
def confirmationpage(request):
    return render(request,'confirmation.html')


@login_required(login_url="/login/")
def removewishlistpage(request,num):
    try:
        item=Wishlist.objects.get(id=num)
        item.delete()
    except:
        pass
    return HttpResponseRedirect("/profile/")

@login_required(login_url="/login/")
def profilepage(request):
    user=User.objects.get(username=request.user.username)
    if(user.is_superuser):
                return HttpResponseRedirect("/admin/")
    else:
        buyer=Buyers.objects.get(username=request.user.username)
        wishlist=Wishlist.objects.filter(buyer=buyer)
        checkout=Checkout.objects.filter(buyer=buyer)
        orders=[]
        for item in checkout:
            cp=CheckoutProducts.objects.filter(checkout=item.id)
            orders.append({'checkout':item,'checkoutProducts':cp})
        
        return render(request,"profile.html",{'data':buyer,'wishlist':wishlist,'orders':orders})
@login_required(login_url="/login/")
def updateprofile(request):
    user=User.objects.get(username=request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect("/admin/")
    else:
        buyer=Buyers.objects.get(username=request.user.username)
        if(request.method=="POST"):
            buyer.name=request.POST.get("name")
            buyer.email=request.POST.get("email")
            buyer.phone=request.POST.get("phone")
            buyer.addressline1=request.POST.get("addressline1")
            buyer.addressline2=request.POST.get("addressline2")
            buyer.addressline3=request.POST.get("addressline3")
            buyer.pin=request.POST.get("pin")
            buyer.city=request.POST.get("city")
            buyer.state=request.POST.get("state")
            if(request.FILES.get("pic")!=None):
                buyer.pic=request.FILES.get("pic")
            buyer.save()
            return HttpResponseRedirect("/profile/")
    return render(request,"update-profile.html",{'data':buyer})

def forgotpasswordpage1(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        try:
            user=Buyers.objects.get(username=username)
            otp=randint(100000,999999)
            user.otp=otp
            user.save()
            request.session['reset-password-username']=username
            subject = 'Otp for password reset: FashionWorld'
            message = """
                      Hello """+user.name+""""
                      OTP for password reset is """+str(otp)+"""
                      Enter the otp on reset password form 
                      Never share otp with anyone
                      Team: FashionWorld
                      """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect("/forgot-password2/")
        except:
            messages.error(request,"Invalid Username")
    return render(request,"forgot-password1.html")

def forgotpasswordpage2(request):
    if(request.method=="POST"):
        otp=int(request.POST.get("otp"))
        try:
            user=Buyers.objects.get(username=request.session.get("reset-password-username",None))
            if(otp==user.otp):
               return HttpResponseRedirect("/forgot-password3/")
            else:
                messages.error(request,"Invalid OTP")

            
        except:
            messages.error(request,"Un-Authorized")
   
    return render(request,"forgot-password2.html")

def forgotpasswordpage3(request):
    if(request.method=="POST"):
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if(password==cpassword):
            try:
                user=User.objects.get(username=request.session.get("reset-password-username",None))
                user.set_password(password)
                user.save()
                if(request.session['reset-password-username']):
                     del request.session['reset-password-username']

                return HttpResponseRedirect("/login/")
            except:
                messages.error(request,"Un-Authorized")
        else:
            messages.error(request,"password and confirm password not matched")   
    return render(request,"forgot-password3.html")

def logoutpage(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")