
from .models import Order
from .serializers import Orderserializers
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
# Create your views here.



def valid_user_sessions(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk =id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist as e:
        return False
    

@csrf_exempt
def add(request,id,token):
    if not valid_user_sessions(user_id,token):
        return JsonResponse({'error':"please re-login",'code':'500'})
    

    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST['transaction_id']
        ammount = request.POST['ammount']
        product= request.POST['ammount']

        total_product = len(product.split(',')[-1])

        userModel = get_user_model

        try:
            user = userModel.objects.get(pk = id)

        except userModel.DoesNotExist  as e:
              return JsonResponse({'error':"user does not exsit",'code':'500'})
        
        ordr = Order(user = user, product_name=product, total_product=total_product,transaction_id=transaction_id, total_ammount = ammount )
        ordr.save()
        return JsonResponse({'succes':True,'error':False,'msg': 'order place successfully'})
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset =Order.objects.all().order_by('product_name')
    serializer_class = Orderserializers