from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from accounts import serializers
from users.models import User
from .models import Account



# Create your views here.

@api_view(["GET"])
def account_details(request):
    try:
        account_details = Account.objects.get(user=request.user.id)
    except Account.DoesNotExist:
        return Response({"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.AccountDetails(account_details)
    return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    




@api_view(['POST'])
def create_account(request):
    user = request.user.id
    account_data = request.data.copy()
    account_data['user'] = user
    
    serializer = serializers.CreateAccount(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message": "your Account has been created successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({'messsage':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['DELETE'])
def delete_account(request):
    user = request.user.id
    try:
        user = User.objects.get(id=user)
    except User.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    