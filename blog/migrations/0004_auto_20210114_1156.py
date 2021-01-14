# Generated by Django 3.1.5 on 2021-01-14 02:56

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, validators=[blog.models.min_length_3_validator]),
        ),
    ]
