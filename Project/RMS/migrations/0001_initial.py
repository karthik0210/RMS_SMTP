# Generated by Django 5.0.6 on 2024-05-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='smtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=256)),
                ('Location', models.CharField(max_length=256)),
                ('Message', models.CharField(max_length=256)),
            ],
        ),
    ]
