from django.db import models

# Create your models here.
class User(models.Model):
    telephone = models.CharField(max_length=12)
    namehotel = models.CharField(max_length=50)
    roomhotel = models.CharField(max_length=15)
    pirec_room = models.FloatField(max_length=50)
    quantity_people = models.CharField(max_length=50)
    date_checkin = models.DateTimeField(auto_now_add=True)
    date_checkout = models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.telephone


class Hotel(models.Model):
    namehotel = models.CharField(max_length=50)
    room_normal_price = models.FloatField(max_length=50)
    room_vip_price = models.FloatField(max_length=50)

    def __str__(self):
        return self.namehotel

class Phone_Number(models.Model):
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.phone