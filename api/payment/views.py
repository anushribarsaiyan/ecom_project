from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree


import braintree

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
      braintree.Environment.Sandbox,
      merchant_id="mg3f4qnyg75b2mst",
      public_key="qw2m32jqrbfdpvgc",
      private_key="56d3beaae2e4ab89ed4bfb030b064e45"
  )
)


def validate_user_session(id,token):
    userModel = get_user_model()
    try:
        user = userModel.objects.get(id=id)
        if user.session_token == token:
            return True
        else:
            return False
    except userModel.DoesNotExist:
        return False
    

@csrf_exempt
def genrate_token(request, id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':"Invalid token"})
    
    return  JsonResponse({'clientToken': gateway.client_token, 'success':"true"})

@csrf_exempt
def process_payment(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':"Invalid token"})
    
    nonce_from_the_client = request.POST['paymentMethodNonce']
    ammount_from_the_client = request.POST['paymentMethodNonce']

    result = gateway.transaction.sale({
    "amount": ammount_from_the_client,
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }
})
    if result.is_success:
        return JsonResponse({"success": result.is_success, 'transaction':{'id': result.transaction.id,'amount': result.amount.id}})
    
    else:
        return JsonResponse({"success": False})

    
    



       

    
