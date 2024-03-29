# Generated by Django 5.0.1 on 2024-02-05 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='posts.category'),
        ),
    ]
