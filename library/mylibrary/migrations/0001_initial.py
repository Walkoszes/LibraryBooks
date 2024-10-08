# Generated by Django 5.1.1 on 2024-09-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=100, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['author'],
                'indexes': [models.Index(fields=['isbn'], name='isbn_idx')],
            },
        ),
    ]
