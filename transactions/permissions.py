from rest_framework.permissions import BasePermission
from accounts.models import Account


class IscurrentAccount(BasePermission):
    message = "You do not have permission to perform this action."
    
    def has_permission(self, request, view):
        try:
         user_account = Account.objects.get(user=request.user.id)
        except Account.DoesNotExist:
            return False
        if request.method in ["POST"] and user_account.account_type == "current":
            return True
        else:
            return False