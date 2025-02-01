# Generated by Django 5.1.5 on 2025-01-30 08:36

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
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('organisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisateur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validation', models.BooleanField(default=False)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='App_gestion_Evenement.evenement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateTimeField(auto_now_add=True)),
                ('acheteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='App_gestion_Evenement.evenement')),
            ],
        ),
    ]
