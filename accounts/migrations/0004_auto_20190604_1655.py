# Generated by Django 2.0.13 on 2019-06-04 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190604_0027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='note',
            name='name',
        ),
        migrations.RemoveField(
            model_name='note',
            name='title',
        ),
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]