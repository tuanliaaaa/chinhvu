# Generated by Django 4.1.7 on 2023-04-16 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entity', '0006_alter_categoryfilm_category_alter_categoryfilm_film_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryfilm',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryfilm', to='Entity.category'),
        ),
        migrations.AlterField(
            model_name='categoryfilm',
            name='Film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryfilm', to='Entity.film'),
        ),
    ]