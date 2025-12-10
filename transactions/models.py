from django.db import models

# Create your models here.

#model your models here. self referencial model relationship
    
class Transactions(models.Model):
      sender = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='sent_transactions')
      receiver = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='received_transactions')
      amount = models.FloatField(null=True, blank=True)
      status = models.CharField(max_length=20)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      
def __str__(self):
          return f"Transaction from {self.sender} to {self.receiver} - {self.status}"