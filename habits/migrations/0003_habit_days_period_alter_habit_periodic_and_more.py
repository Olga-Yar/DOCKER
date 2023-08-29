# Generated by Django 4.2.4 on 2023-08-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='days_period',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], default='1', verbose_name='день недели'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodic',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly')], default='daily', verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(default=None, max_length=50, verbose_name='вознаграждение'),
        ),
    ]
