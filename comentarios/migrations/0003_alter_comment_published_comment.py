# Generated by Django 3.2.2 on 2021-05-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_comment_user_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_comment',
            field=models.BooleanField(default=False),
        ),
    ]
