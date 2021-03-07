# Generated by Django 3.1.6 on 2021-03-07 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_remove_userinfo_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='propic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profileimages',
        ),
    ]