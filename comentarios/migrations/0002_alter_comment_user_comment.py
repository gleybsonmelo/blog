# Generated by Django 3.2.2 on 2021-05-12 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
