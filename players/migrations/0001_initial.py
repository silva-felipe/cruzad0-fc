# Generated by Django 4.1.5 on 2023-02-01 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('favorite_team', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='players')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.position')),
            ],
        ),
    ]
