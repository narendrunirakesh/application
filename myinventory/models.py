from django.db import models

class InventoryItem(models.Model):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
    ]

    # product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    batch_num = models.CharField(max_length=50)
    batch_date = models.DateField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.product_name
