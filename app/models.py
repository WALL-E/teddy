from django.db import models

# Create your models here.

import json
import uuid

from django.db import models


class BaseObject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderSide(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False, unique=True)
    code = models.IntegerField(null=False, default=0)
    priority = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OrderSide'
        verbose_name_plural = 'OrderSides'


class OrderType(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False, unique=True)
    code = models.IntegerField(null=False, default=0)
    priority = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OrderType'
        verbose_name_plural = 'OrderTypes'


class OrderRule(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False, unique=True)
    code = models.IntegerField(null=False, default=0)
    priority = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OrderRule'
        verbose_name_plural = 'OrderRules'



class Currencie(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currencie'
        verbose_name_plural = 'Currencies'


class Symbol(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False, unique=True)
    base_currency = models.CharField(max_length=64, null=False, unique=False)
    quote_currency = models.CharField(max_length=64, null=False, unique=False)
    price_decimal = models.IntegerField(null=False, default=0)
    amount_decimal = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Symbol'
        verbose_name_plural = 'Symbols'
        unique_together = (("base_currency", "quote_currency"),)


class Balance(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency = models.CharField(max_length=64, null=False, unique=True)
    category = models.CharField(max_length=64, null=False, unique=False)
    available = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)
    frozen = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)
    balance = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)

    def __str__(self):
        return self.currency

    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        unique_together = (('currency', 'category'),)



class Certification(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False, unique=True)
    desc = models.CharField(max_length=255, null=False, default="")
    key = models.CharField(max_length=255, null=False, default="")
    secret = models.CharField(max_length=255, null=False, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'


class Account(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    certification = models.ForeignKey(Certification, on_delete=False)
    additional = models.CharField(max_length=255, null=False, default="")

    def __str__(self):
        return self.certification.name

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class Biz(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.CharField(max_length=128, default="", unique=True)
    order_symbol = models.ForeignKey(Symbol, on_delete=False)
    order_side = models.ForeignKey(OrderSide, on_delete=False)
    order_type = models.ForeignKey(OrderType, on_delete=False)
    order_price = models.CharField(max_length=128, null=False, default="")
    order_amount = models.CharField(max_length=128, null=False, default="")
    order_state  = models.CharField(max_length=128, null=True, default="")
    order_executed_value = models.CharField(max_length=128, null=True, default="")
    order_filled_amount= models.CharField(max_length=128, null=True, default="")
    order_fill_fees = models.CharField(max_length=128, null=True, default="")
    order_created_at = models.CharField(max_length=128, null=True, default="")
    order_source = models.CharField(max_length=128, null=True, default="")

    def __str__(self):
        return self.order_id


    def save(self, *args, **kwargs):
        print("biz biz biz")
        super(Biz, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Biz'
        verbose_name_plural = 'Bizs'


class TradingStrategy(BaseObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False, unique=False)
    price = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)
    order_rule =  models.ForeignKey(OrderRule, on_delete=False)
    order_side =  models.ForeignKey(OrderSide, on_delete=False)
    amount = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)
    total = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)
    interval = models.DecimalField(max_digits=40, decimal_places=18, default=0, null=False)
    enable = models.BooleanField(null=False, default=False)
    username = models.CharField(max_length=64, null=False, unique=False)

    def __str__(self):
        return self.name

   
    def save(self, *args, **kwargs):
        super(TradingStrategy, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'TradingStrategy'
        verbose_name_plural = 'TradingStrategys'
