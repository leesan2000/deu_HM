# Generated by Django 4.2.3 on 2023-08-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('H', 'Masculino'), ('M', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
    ]
