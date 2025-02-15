from django.db import models

class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Entrepreneur'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    product_name = models.CharField(max_length=255)
    product_model = models.CharField(max_length=255)
    release_date = models.DateField()
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='supplied_nodes')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name
