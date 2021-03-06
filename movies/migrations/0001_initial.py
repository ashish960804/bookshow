# Generated by Django 3.2.7 on 2021-10-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cast', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=20)),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('BENGALI', 'Bengali'), ('HINDI', 'Hindi'), ('TAMIL', 'Tamil'), ('TELUGU', 'Telugu'), ('MALAYALAM', 'Malayalam'), ('MARATHI', 'Marathi'), ('FRENCH', 'French')], max_length=10)),
                ('run_length', models.IntegerField(help_text='Enter run length in minutes')),
                ('certificate', models.CharField(choices=[('U', 'U'), ('UA', 'U/A'), ('A', 'A'), ('R', 'R')], max_length=2)),
                ('popularity_index', models.IntegerField(blank=True, null=True, unique=True)),
                ('trailer', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
