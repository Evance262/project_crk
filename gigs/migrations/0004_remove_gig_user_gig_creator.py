# Generated by Django 4.0.4 on 2022-05-31 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0003_gig_users_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='user',
        ),
        migrations.AddField(
            model_name='gig',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
