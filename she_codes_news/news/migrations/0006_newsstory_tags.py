# Generated by Django 4.2.2 on 2023-07-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='tags',
            field=models.ManyToManyField(to='news.tag'),
        ),
    ]
