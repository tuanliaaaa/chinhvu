# Generated by Django 4.1.7 on 2023-04-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entity', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='FullName',
            field=models.CharField(max_length=225, null=True),
        ),
    ]