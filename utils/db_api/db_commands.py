from asgiref.sync import sync_to_async
from django.db import InterfaceError, connection

from course_project.admin_panel.models import Users, CourseProgress, Courses


@sync_to_async()
def create_user(telegram_id, name, username):
    """
    Функция, создающая запись пользователя в таблице admin_panel_users
    """
    try:
        return Users.objects.get_or_create(
            telegram_id=telegram_id,
            name=name,
            username=username
        )
    except InterfaceError:
        connection.close()


@sync_to_async()
def get_user(telegram_id):
    """
    Функция, возвращающая запись пользователя из таблицы admin_panel_users
    """
    try:
        return Users.objects.filter(telegram_id=telegram_id).first()
    except InterfaceError:
        connection.close()


@sync_to_async()
def update_github(telegram_id, link):
    """
    Функция для обновления ссылки на GitHub
    """
    try:
        Users.objects.filter(telegram_id=telegram_id).update(github_link=link)
    except InterfaceError:
        connection.close()


@sync_to_async()
def get_course_progress(telegram_id):
    """
    Функция, возвращающая информацию о студенте из таблицы admin_panel_courseprogrress
    """
    try:
        return CourseProgress.objects.filter(student__telegram_id=telegram_id).first()

    except InterfaceError:
        connection.close()


@sync_to_async()
def get_courses():
    """
    Функция, возвращающая все курсы для клавиатуры
    """
    try:
        return Courses.objects.order_by('pk').all()
    except InterfaceError:
        connection.close()


@sync_to_async()
def get_course_db(pk):
    """
    Функция, возвращающая курс по ключу (pk)
    """
    try:
        return Courses.objects.filter(pk=pk).first()
    except InterfaceError:
        connection.close()
