# Generated by Django 5.0 on 2024-01-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_articlecategory_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, unique=True, verbose_name='عنوان در url')),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='تصویر')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('text', models.TextField(verbose_name='متن اصلی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('selected_categories', models.ManyToManyField(to='article_module.articlecategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]