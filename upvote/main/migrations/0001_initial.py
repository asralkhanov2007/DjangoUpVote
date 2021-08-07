# Generated by Django 3.2.5 on 2021-08-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title...')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='*')),
                ('image', models.ImageField(upload_to='media/UpVoteImages/', verbose_name='Image...')),
                ('body', models.TextField(verbose_name='Body....')),
            ],
            options={
                'verbose_name': 'Upvote',
                'verbose_name_plural': 'Upvotes',
            },
        ),
    ]