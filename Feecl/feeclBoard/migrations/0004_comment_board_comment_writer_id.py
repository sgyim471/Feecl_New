# Generated by Django 3.2.5 on 2021-11-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeclBoard', '0003_comment_board_comment_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_board',
            name='comment_writer_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
