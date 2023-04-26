# Generated by Django 4.1.7 on 2023-04-26 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entity', '0023_rename_actorfilm_actorchapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actorchapter',
            name='Actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actorchapter', to='Entity.actor'),
        ),
        migrations.AlterField(
            model_name='actorchapter',
            name='Chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapteractor', to='Entity.chapter'),
        ),
    ]