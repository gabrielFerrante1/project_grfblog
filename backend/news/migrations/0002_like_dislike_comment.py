# Generated by Django 4.1.2 on 2022-11-05 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.notice')),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.notice')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.notice')),
            ],
        ),
    ]
