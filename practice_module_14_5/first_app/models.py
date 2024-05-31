from django.db import models

# Create your models here.
class Model_data(models.Model):
    id = models.AutoField(primary_key=True)

    integer_field = models.IntegerField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    float_field = models.FloatField()

    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=20)
    address = models.TextField()

    email_field = models.EmailField()
    url_field = models.URLField()

    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()

    file_field = models.FileField(upload_to='files/')
    

    checked = models.BooleanField()



