# Generated by Django 4.2.3 on 2023-07-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_timer_s2_send_timer_s2_timer_timer_s3_send_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='users',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
    ]
