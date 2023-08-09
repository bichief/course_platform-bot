from rest_framework import serializers

from course_project.admin_panel.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'telegram_id', 'name', 'username', 'amount_refferal', 'amount_rating', 'connect_date', 'rating',
                  'refferal_balance')
