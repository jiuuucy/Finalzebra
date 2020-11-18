# Generated by Django 3.1.3 on 2020-11-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zebraapp', '0003_myitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('cover', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='TipBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zebraapp.tip')),
            ],
        ),
    ]