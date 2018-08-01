# Generated by Django 2.0.7 on 2018-08-01 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_orderrule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradingstrategy',
            name='rule',
        ),
        migrations.AddField(
            model_name='tradingstrategy',
            name='order_rule',
            field=models.ForeignKey(default='80b92b360c1e40118d177123fb73ad53', on_delete=False, to='app.OrderRule'),
            preserve_default=False,
        ),
    ]
