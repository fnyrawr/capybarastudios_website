# Generated by Django 4.1.5 on 2023-01-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0004_alter_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(default='Project & Management', max_length=15),
        ),
    ]
