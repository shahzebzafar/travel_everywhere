# Generated by Django 2.2.3 on 2020-03-19 17:51

from django.db import migrations, models
import django.db.models.deletion
import traveleverywhere.models


class Migration(migrations.Migration):

    dependencies = [
        ('traveleverywhere', '0007_auto_20200319_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog_image',
            name='blog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='traveleverywhere.Blog'),
        ),
        migrations.AlterField(
            model_name='blog_image',
            name='image',
            field=models.ImageField(upload_to=traveleverywhere.models.get_image_filename, verbose_name='Image'),
        ),
    ]