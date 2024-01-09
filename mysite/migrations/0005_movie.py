# Generated by Django 4.2.6 on 2024-01-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('action', '動作片'), ('romance', '愛情片'), ('drama', '劇情片')], max_length=20)),
                ('release_year', models.IntegerField()),
            ],
        ),
    ]