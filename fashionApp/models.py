from django.db import models

class Maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="brand",default=None,blank=True,null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    maincategory=models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.CharField(max_length=50)
    final_price=models.CharField(max_length=20)
    base_price=models.CharField(max_length=20,blank=True,null=True)
    discount=models.CharField(max_length=30,blank=True,null=True)
    delivery=models.CharField(max_length=300,default=None,blank=True,null=True)
    description=models.TextField(default=None,blank=True,null=True)
   
    pic1=models.ImageField(upload_to="product")
    pic2=models.ImageField(upload_to="product",default=None,blank=True,null=True)
    pic3=models.ImageField(upload_to="product",default=None,blank=True,null=True)
    pic4=models.ImageField(upload_to="product",default=None,blank=True,null=True)
    pic5=models.ImageField(upload_to="product",default=None,blank=True,null=True)
    def __str__(self):
        return self.name

class testimonial(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="testimonial",blank=True,null=True)
    name=models.CharField(max_length=200)
    message=models.TextField()
    def __str__(self):
        return self.name


class Buyers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,default="")
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    addressline1=models.CharField(max_length=100,default="",null=True,blank=True)
    addressline2=models.CharField(max_length=100,default="",null=True,blank=True)
    addressline3=models.CharField(max_length=100,default="",null=True,blank=True)
    pin=models.CharField(max_length=10,default="",null=True,blank=True)
    city=models.CharField(max_length=30,default="",null=True,blank=True)
    state=models.CharField(max_length=30,default="",null=True,blank=True)
    pic=models.ImageField(upload_to="buyers",default="",null=True,blank=True)
    otp=models.IntegerField(default=-12333111)

    def __str__(self):
        return self.name+"/"+self.email
    
class Wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    buyer=models.ForeignKey(Buyers,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default="")

    def __str__(self):
        return str(self.id)+"/"+self.buyer.username
    
paymentMode=((1,"COD"),(2,"Net Banking")) 
paymentStatus=((1,"Pending"),(2,"Done"))
orderStatus=((1,"Order Placed"),(2,"Order is Dispatch"),(3," Dispatched"),(4,"Out for Delivery"),(5,"Delivered"))
class Checkout(models.Model):
    id=models.AutoField(primary_key=True)
    buyer=models.ForeignKey(Buyers,on_delete=models.CASCADE)
    paymentMode=models.IntegerField(choices=paymentMode,default=1)
    paymentStatus=models.IntegerField(choices=paymentStatus,default=1)
    orderStatus=models.IntegerField(choices=orderStatus,default=1)
    subtotal=models.IntegerField()
    shipping=models.IntegerField()
    final=models.IntegerField()
    rppid=models.CharField(max_length=30,default="")
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+"/"+self.buyer.username
    
class CheckoutProducts(models.Model):
    id=models.AutoField(primary_key=True)
    checkout=models.ForeignKey(Checkout,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    total=models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+"/"+str(self.checkout.id)+"/"+self.product.name
contactstatus=((1,"Active"),(2,"Done"))   
class contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    status=models.IntegerField(choices=contactstatus,default=1)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+"/"+self.name+"/"+self.email
       