# Generated by Django 4.1.7 on 2023-02-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_notice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(default='', upload_to='notice/images'),
        ),
    ]