# Generated by Django 5.0.7 on 2024-08-21 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0007_rename_reviews_watchreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_count', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.watchupload')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Homepage.cart')),
            ],
        ),
    ]
