# Generated by Django 5.2.1 on 2025-06-06 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TarefaAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=55)),
                ('status', models.BooleanField(default=False)),
                ('data_entrega', models.DateTimeField(auto_now_add=True)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
