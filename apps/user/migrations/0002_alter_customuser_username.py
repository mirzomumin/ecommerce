# Generated by Django 4.1.2 on 2022-10-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
    ]