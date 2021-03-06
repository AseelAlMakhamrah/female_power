# Generated by Django 2.2.4 on 2020-12-25 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whcapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='whcapp.User')),
                ('skills', models.TextField()),
                ('education', models.TextField()),
                ('education_from', models.CharField(max_length=45)),
                ('education_to', models.CharField(max_length=45)),
                ('experience', models.TextField()),
                ('experience_from', models.CharField(max_length=45)),
                ('experience_to', models.CharField(max_length=45)),
                ('links', models.TextField()),
                ('video_url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
