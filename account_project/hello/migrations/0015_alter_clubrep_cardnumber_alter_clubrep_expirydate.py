# Generated by Django 4.1.2 on 2023-01-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_alter_clubrep_expirydate_alter_clubrep_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubrep',
            name='cardNumber',
            field=models.IntegerField(max_length=19),
        ),
        migrations.AlterField(
            model_name='clubrep',
            name='expiryDate',
            field=models.CharField(max_length=8),
        ),
    ]
