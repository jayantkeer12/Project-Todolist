# Generated by Django 4.0.6 on 2022-07-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_uploadimage_alter_todolistiteam_e_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to='shop\\images'),
        ),
    ]
