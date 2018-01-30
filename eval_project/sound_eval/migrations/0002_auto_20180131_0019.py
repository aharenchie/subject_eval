# Generated by Django 2.0 on 2018-01-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound_eval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(default=100)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(default=100),
        ),
    ]