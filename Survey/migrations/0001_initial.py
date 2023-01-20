# Generated by Django 4.1.5 on 2023-01-20 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], max_length=1)),
                ('question', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('review', models.TextField()),
                ('wishes', models.TextField(blank=True)),
                ('gameidea', models.CharField(choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], default=3, max_length=1)),
                ('gamedesign', models.CharField(choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], default=3, max_length=1)),
                ('gameplay', models.CharField(blank=True, choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], default=3, max_length=1)),
                ('websiteDesign', models.CharField(choices=[('1', 'Meh'), ('2', 'Lame'), ('3', 'Mid'), ('4', 'Good'), ('5', 'Awesome')], default=3, max_length=1)),
                ('timestamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Survey',
                'verbose_name_plural': 'Surveys',
                'ordering': ['timestamp'],
            },
        ),
    ]