# Generated by Django 4.2.3 on 2023-07-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_timer_s1_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='s2_send',
            field=models.BooleanField(default=False, help_text='Да/нет', verbose_name='Отправили напоминание через 2 часа'),
        ),
        migrations.AddField(
            model_name='timer',
            name='s2_timer',
            field=models.DateTimeField(help_text='Таймер на 2 часа', null=True, verbose_name='Когда отправляем уведомление'),
        ),
        migrations.AddField(
            model_name='timer',
            name='s3_send',
            field=models.BooleanField(default=False, help_text='Да/нет', verbose_name='Отправили напоминание через 6 часов?'),
        ),
        migrations.AddField(
            model_name='timer',
            name='s3_timer',
            field=models.DateTimeField(help_text='Таймер на 6 часов', null=True, verbose_name='Когда отправляем уведомление'),
        ),
        migrations.AddField(
            model_name='timer',
            name='s4_send',
            field=models.BooleanField(default=False, help_text='Да/нет', verbose_name='Отправили напоминание через 24 часа?'),
        ),
        migrations.AddField(
            model_name='timer',
            name='s4_timer',
            field=models.DateTimeField(help_text='Таймер на 24 часа', null=True, verbose_name='Когда отправляем уведомление'),
        ),
        migrations.AlterField(
            model_name='timer',
            name='s1_send',
            field=models.BooleanField(default=False, help_text='Да/нет', verbose_name='Отправили напоминание через 2 часа?'),
        ),
    ]
