# Generated by Django 2.2.3 on 2020-03-27 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('traveleverywhere', '0016_auto_20200327_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='users',
        ),
        migrations.RemoveField(
            model_name='airline',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='airline',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='airline',
            name='users',
        ),
        migrations.RemoveField(
            model_name='bookingwebsite',
            name='users',
        ),
        migrations.AddField(
            model_name='agency',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookingwebsite',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AirlineLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveleverywhere.Airline')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AirlineDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveleverywhere.Airline')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
