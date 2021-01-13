from django.db import models

class BackUpCopy(models.Model):
    name_of_copy = models.CharField(max_length=45)
    type_of_copy = models.CharField(max_length=45)
    creation_date = models.DateField()
    commentary = models.CharField(max_length=100)

class Tariff(models.Model):
    date = models.DateField()
    settlment = models.CharField(max_length=45)
    cost_per_minute = models.FloatField()
    preferential_cost = models.FloatField()
    objects = models.Manager()

class paid_receipt(models.Model):
    id_receipt = models.IntegerField()
    payment = models.CharField(max_length=45)
    objects = models.Manager()

class Receipt(models.Model):
    number = models.CharField(max_length=45)
    date = models.DateField()
    cost = models.FloatField()
    payment_term = models.DateField()
    id_paid = models.ForeignKey('paid_receipt', on_delete=models.CASCADE)
    id_tariff = models.ForeignKey('Tariff', on_delete=models.CASCADE)
    id_tconversation = models.ForeignKey('TelephoneConversation', on_delete=models.CASCADE)
    objects = models.Manager()

class TelephoneConversation(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    call_duration = models.FloatField()
    id_conversation = models.IntegerField()
    objects = models.Manager()


class Client(models.Model):
    number = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    registration_date = models.DateField()
    id_receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE)
    objects = models.Manager()

class User(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    id_receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)
    objects = models.Manager()











