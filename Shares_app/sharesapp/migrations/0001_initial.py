# Generated by Django 5.0.4 on 2024-04-05 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShareDetails',
            fields=[
                ('s_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('companyshare', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.BigIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserShare', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
