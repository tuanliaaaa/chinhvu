# Generated by Django 4.1.7 on 2023-04-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entity', '0017_alter_chapter_chapterdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='ChapterDescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='ChapterImage',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='ChapterStatus',
            field=models.CharField(max_length=225),
        ),
    ]
