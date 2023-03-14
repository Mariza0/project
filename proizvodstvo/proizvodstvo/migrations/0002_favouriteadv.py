# Generated by Django 4.1.7 on 2023-02-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proizvodstvo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteAdv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('fav_adv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proizvodstvo.advertisement')),
            ],
        ),
    ]
