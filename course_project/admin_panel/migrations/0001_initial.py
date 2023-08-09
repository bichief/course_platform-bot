# Generated by Django 4.2.3 on 2023-07-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.BigIntegerField(help_text='Telegram ID пользователя', verbose_name='Telegram ID пользователя')),
                ('name', models.CharField(help_text='Имя', max_length=1000, null=True, verbose_name='Имя')),
                ('username', models.CharField(help_text='Имя пользователя', max_length=1000, null=True, verbose_name='Имя пользователя')),
                ('sub_channel', models.BooleanField(default=False, help_text='Подписан на канал?', verbose_name='Подписан на канал?')),
                ('refferal_id', models.BigIntegerField(help_text='Пригласивший', null=True, verbose_name='Пригласивший')),
                ('from_where', models.CharField(help_text='Какой вход?', max_length=500, null=True, verbose_name='Какой вход?')),
            ],
        ),
    ]
