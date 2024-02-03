# Generated by Django 5.0 on 2024-01-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='title', max_length=300, verbose_name='عنوان در url'),
            preserve_default=False,
        ),
    ]