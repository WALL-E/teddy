# Generated by Django 2.0.7 on 2018-07-31 07:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('currency', models.CharField(max_length=64, unique=True)),
                ('category', models.CharField(max_length=64)),
                ('available', models.DecimalField(decimal_places=18, default=0, max_digits=40)),
                ('frozen', models.DecimalField(decimal_places=18, default=0, max_digits=40)),
                ('balance', models.DecimalField(decimal_places=18, default=0, max_digits=40)),
            ],
            options={
                'verbose_name': 'Balance',
                'verbose_name_plural': 'Balances',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('desc', models.CharField(default='', max_length=255)),
                ('key', models.CharField(default='', max_length=255)),
                ('secret', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
            },
        ),
        migrations.CreateModel(
            name='Currencie',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Currencie',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('additional', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Current',
                'verbose_name_plural': 'Currents',
            },
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('base_currency', models.CharField(max_length=64)),
                ('quote_currency', models.CharField(max_length=64)),
                ('price_decimal', models.IntegerField(default=0)),
                ('amount_decimal', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Symbol',
                'verbose_name_plural': 'Symbols',
            },
        ),
        migrations.AlterUniqueTogether(
            name='symbol',
            unique_together={('base_currency', 'quote_currency')},
        ),
    ]
