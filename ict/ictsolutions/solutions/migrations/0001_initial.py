# Generated by Django 5.1.4 on 2024-12-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('clase', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
