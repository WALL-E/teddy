# Generated by Django 2.0.7 on 2018-07-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180731_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biz',
            name='order_symbol',
            field=models.ForeignKey(on_delete=False, to='app.Symbol'),
        ),
    ]
