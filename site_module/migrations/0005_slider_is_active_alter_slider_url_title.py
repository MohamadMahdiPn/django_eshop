# Generated by Django 5.0 on 2024-01-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_slider_alter_footerlink_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_Active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_title',
            field=models.CharField(max_length=255, verbose_name='عنوان لینک'),
        ),
    ]