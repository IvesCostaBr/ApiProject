# Generated by Django 3.2.5 on 2021-07-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]