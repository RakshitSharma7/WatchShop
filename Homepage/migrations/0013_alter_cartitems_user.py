# Generated by Django 4.2.15 on 2024-08-31 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0012_alter_cartitems_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Homepage.cart'),
        ),
    ]
