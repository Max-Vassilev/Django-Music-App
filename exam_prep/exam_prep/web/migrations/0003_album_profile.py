# Generated by Django 4.2.2 on 2023-06-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='web.profile'),
            preserve_default=False,
        ),
    ]
