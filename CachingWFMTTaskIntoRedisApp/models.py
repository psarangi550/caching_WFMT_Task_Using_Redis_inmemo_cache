from django.db import models

# Create your models here.

class Category(models.Model):
    site=models.CharField(max_length=10)
    
    def __str__(self):
        return self.site


class WFMTTaskModel(models.Model):
    cp_number = models.CharField(max_length=10)
    sne_id=models.IntegerField()
    scheme_number=models.IntegerField()
    trs=models.CharField(max_length=2)
    estimate=models.CharField(max_length=10)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cp_number
    