# Generated by Django 3.0.6 on 2020-07-03 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_student_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_Student', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
