import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Levels(models.Model):
    level_title = models.CharField(
        verbose_name='Название уровня',
        max_length=500,
        null=True
    )

    rating_amount = models.IntegerField(
        verbose_name='Необходимое количество очков для перехода',
        null=True
    )

    def __str__(self):
        return self.level_title


class Users(models.Model):
    telegram_id = models.BigIntegerField(
        verbose_name='Telegram ID',
        help_text='Telegram ID'
    )

    name = models.CharField(
        max_length=500,
        null=True,
        verbose_name='Имя',
        help_text='имя'
    )

    username = models.CharField(
        max_length=500,
        null=True,
        verbose_name='Username',
        help_text='username'
    )

    github_link = models.CharField(
        null=True,
        max_length=1000,
        verbose_name='Ссылка на ГитХаб',
        help_text='Ссылка на ГитХаб'
    )

    level = models.ForeignKey(
        Levels,
        on_delete=models.CASCADE,
        related_name='lvl',
        blank=True,
        null=True,
        help_text='Уровень',
        verbose_name='Уровень',
        default=1
    )

    amount_rating = models.IntegerField(
        verbose_name='Количество очков рейтинга',
        default=0
    )

    learning = models.BooleanField(
        default=False,
        verbose_name='Обучается?'
    )

    amount_ref = models.IntegerField(
        verbose_name='Количество приглашенных',
        default=0
    )
    balance_ref = models.IntegerField(
        verbose_name='Реферальный баланс',
        default=0
    )
    course_sale = models.IntegerField(
        verbose_name='Скидка на курс, руб.',
        default=0
    )
    ref = models.BigIntegerField(
        verbose_name='Кто пригласил',
        null=True
    )

    ignore = models.BooleanField(
        default=False,
        verbose_name='Игнорщик?'
    )

    notify_vebinar = models.BooleanField(
        default=False,
        verbose_name='Напомнить о вебинаре'
    )

    connect_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата присоединения',
        help_text='дата присоединения'
    )

    def __str__(self):
        return self.name


class Courses(models.Model):
    annotation = models.CharField(
        max_length=6000,
        null=True,
        verbose_name='Аннотация к курсу'
    )

    course_title = models.CharField(
        max_length=5000,
        null=True,
        verbose_name='Название курса',
        help_text='название курса'
    )

    course_description = models.CharField(
        max_length=10000,
        null=True,
        verbose_name='Описание курса'
    )

    amount_lessons = models.IntegerField(
        null=True,
        verbose_name='Количество уроков',
        help_text='количество уроков в курсе'
    )

    price = models.IntegerField(
        null=True,
        verbose_name='Стоимость, руб.',
        help_text='стоимость курса в рублях'
    )

    def __str__(self):
        return self.course_title


class Payments(models.Model):
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='user',
        blank=True,
        null=True,
        help_text='Покупатель',
        verbose_name='Покупатель'
    )

    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        related_name='course_number',
        blank=True,
        null=True,
        help_text='Курс',
        verbose_name='Курс'
    )

    date = models.DateTimeField(
        null=True,
        verbose_name='Дата платежа'
    )

    receipt = models.CharField(
        max_length=5000,
        null=True,
        verbose_name='Чек',
        help_text='Чек об оплате'
    )


class CourseProgress(models.Model):
    student = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='student_course',
        blank=True,
        null=True,
        help_text='Студент',
        verbose_name='Студент'
    )

    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        related_name='title',
        blank=True,
        null=True,
        help_text='Курс',
        verbose_name='Курс'
    )

    lesson = models.IntegerField(
        default=1,
        verbose_name='Урок',
        help_text='номер урока'
    )


class Timer(models.Model):
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='owner_schedule',
        blank=True,
        null=True,
        help_text='Пользователь',
        verbose_name='Пользователь'
    )

    first_timer = models.BooleanField(
        null=True
    )
    second_timer = models.BooleanField(
        null=True
    )
    third_timer = models.BooleanField(
        null=True
    )
    fourth_timer = models.BooleanField(
        null=True
    )
    five_timer = models.BooleanField(
        null=True
    )
    sixth_timer = models.BooleanField(
        null=True
    )
    seventh_timer = models.BooleanField(
        null=True
    )
    eighth_timer = models.BooleanField(
        null=True
    )
    nine_timer = models.BooleanField(
        null=True
    )
    ten_timer = models.BooleanField(
        null=True
    )
    eleven_timer = models.BooleanField(
        null=True
    )
    twelve_timer = models.BooleanField(
        null=True
    )
    thirteen_timer = models.BooleanField(
        null=True
    )
    fourteen_timer = models.BooleanField(
        null=True
    )
    fifteen_timer = models.BooleanField(
        null=True
    )
    sixteen_timer = models.BooleanField(
        null=True
    )
    seventeen_timer = models.BooleanField(
        null=True
    )
    eighteen_timer = models.BooleanField(
        null=True
    )
    nineteen_timer = models.BooleanField(
        null=True
    )
    twenty_timer = models.BooleanField(
        null=True

    )
