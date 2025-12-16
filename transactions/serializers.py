from rest_framework import serializers
from transactions import models



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = ['sender', 'receiver', 'amount', 'status']
        
        
        
        
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanApplications
        fields = "__all__"