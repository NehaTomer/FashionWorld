from django import template
register=template.Library()

@register.filter(name="paymentStatusFilter")
def paymentStatusFilter(request,status):
    if(status==1):
      return "Pending"
    else:
       return "Done"
    
@register.filter(name="paymentModeFilter")
def paymentModeFilter(request,mode):
    if(mode==1):
      return "COD"
    else:
       return "NetBanking"
    
    
# @register.filter(name="paymentModeFilter")
# def paymentModeFilter(request,mode):
#     if(mode==1):
#       return "COD"
#     else:
#        return "NetBanking"
    
    
@register.filter(name="OrderStatusFilter")
def OrderStatusFilter(request,order):
    if(order==1):
      return "Order Placed"
    elif(order==2):
       return "Order Is Dispatch"
    elif(order==3):
       return "Dispatched"
    elif(order==4):
       return "Out for Delivery"
    else:
       return "Delivered"
    
@register.filter(name="checkforRepayment")
def checkforRepayment(request,checkout):
    if(checkout.paymentStatus==1 and checkout.paymentMode==2):
      return True
    else:
       return False