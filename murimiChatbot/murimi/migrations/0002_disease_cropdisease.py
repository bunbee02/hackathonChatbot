# Generated by Django 4.2.1 on 2023-05-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murimi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='diseases')),
            ],
        ),
        migrations.CreateModel(
            name='CropDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='murimi.crop')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='murimi.disease')),
            ],
        ),
    ]
