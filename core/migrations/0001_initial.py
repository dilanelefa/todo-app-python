# Generated by Django 5.0 on 2023-12-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]