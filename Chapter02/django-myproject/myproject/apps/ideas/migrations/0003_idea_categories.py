# Generated by Django 3.0.5 on 2020-04-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20200418_0723'),
        ('ideas', '0002_idea_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='ideas', to='categories.Category', verbose_name='Categories'),
        ),
    ]
