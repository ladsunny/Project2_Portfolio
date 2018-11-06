from django.db import models

# Create your models here.
class tradingjournal(models.Model):
    ticker = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    trade_date = models.DateTimeField()
    action = models.CharField(max_length=20)
    allocation = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    pub_date = models.DateTimeField()
    justification = models.TextField()
    tags = models.CharField(max_length=300)
    prev_allocation = models.DecimalField(null=True,max_digits=5,decimal_places=2)

    def __str__(self):
        return self.company
