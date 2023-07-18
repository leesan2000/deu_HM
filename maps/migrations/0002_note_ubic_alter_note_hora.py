# Generated by Django 4.2.3 on 2023-07-18 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='ubic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.address'),
        ),
        migrations.AlterField(
            model_name='note',
            name='hora',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
