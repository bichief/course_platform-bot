# Generated by Django 4.2.3 on 2023-07-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0008_timer_b4_send_timer_b4_timer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='b4_timer',
            field=models.DateTimeField(help_text='Таймер на 5 минут', null=True, verbose_name='Таймер B4'),
        ),
    ]
