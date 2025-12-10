from django.db import models

# Create your models here.


class Account(models.Model):
  ACCOUNT_TYPE_CHOICES =(
    ("current", "Current"),
    ("savings", "Savings"),
    )
  
  user = models.OneToOneField(
    'users.User',
    on_delete=models.CASCADE, 
    related_name='user_accunnt',
    null=True,
    blank=True
    )
  
  bvn = models.CharField(max_length=11)
  nin = models.CharField(max_length=11)
  account_number = models.CharField(unique=True, max_length=10, null=True, blank=True)
  account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
  amount = models.FloatField(default=0.0)
  create_at = models.DateTimeField(auto_now_add=True)
  
    
  def __str__(self):
    return f"Account: {self.account_number}"
   
  