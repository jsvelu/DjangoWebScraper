from django.db import models

# Create your models here.

class ScrapedData(models.Model):
    url_id=models.AutoField(primary_key=True)
    url_input = models.CharField(max_length=500)
    category=models.CharField(max_length=200)
    product_title=models.CharField(max_length=500)
    product_description=models.TextField()
    product_price=models.CharField(max_length=200)
    product_rating=models.CharField(max_length=15,default=None)
    product_image=models.TextField(default=None)
    scraped_date = models.DateTimeField('date_scraped',auto_now_add = True)
    
    verbose='scrapeddata'