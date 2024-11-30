# Generated by Django 5.1.2 on 2024-11-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='image/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
