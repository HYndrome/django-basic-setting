# Generated by Django 3.2.18 on 2023-05-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
