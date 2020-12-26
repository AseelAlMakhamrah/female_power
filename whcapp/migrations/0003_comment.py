# Generated by Django 2.2.4 on 2020-12-26 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whcapp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_comments', to='whcapp.Post')),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_comments', to='whcapp.User')),
            ],
        ),
    ]