# Generated by Django 3.2.5 on 2021-09-16 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent_website', '0002_remove_apartments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rent_website.user'),
            preserve_default=False,
        ),
    ]
