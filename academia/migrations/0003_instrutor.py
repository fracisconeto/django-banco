# Generated by Django 5.1.3 on 2024-11-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0002_instituicao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=1000)),
                ('data_nacimento', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]