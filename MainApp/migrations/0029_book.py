# Generated by Django 3.2.10 on 2022-07-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0028_auto_20220702_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('avtor', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
