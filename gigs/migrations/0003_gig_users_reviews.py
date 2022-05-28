# Generated by Django 4.0.4 on 2022-05-22 14:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0002_remove_gig_url_gig_added_files_gig_colors_included_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='users_reviews',
            field=models.ManyToManyField(blank=True, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
