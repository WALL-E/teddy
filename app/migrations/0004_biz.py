# Generated by Django 2.0.7 on 2018-07-31 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180731_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biz',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=128, null=True, unique=True)),
                ('order_symbol', models.CharField(default='', max_length=128)),
                ('order_side', models.CharField(default='', max_length=128)),
                ('order_type', models.CharField(default='', max_length=128)),
                ('order_price', models.CharField(default='', max_length=128)),
                ('order_amount', models.CharField(default='', max_length=128)),
                ('order_state', models.CharField(default='', max_length=128, null=True)),
                ('order_executed_value', models.CharField(default='', max_length=128, null=True)),
                ('order_filled_amount', models.CharField(default='', max_length=128, null=True)),
                ('order_fill_fees', models.CharField(default='', max_length=128, null=True)),
                ('order_created_at', models.CharField(default='', max_length=128, null=True)),
                ('order_source', models.CharField(default='', max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Biz',
                'verbose_name_plural': 'Bizs',
            },
        ),
    ]
