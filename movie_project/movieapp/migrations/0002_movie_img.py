# Generated by Django 4.2.5 on 2023-10-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfbdfbdfdh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]