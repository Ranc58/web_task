# Generated by Django 2.1 on 2018-08-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in queue', 'In Queue'), ('run', 'Run'), ('completed', 'Completed')], default='in queue', max_length=25, verbose_name='Status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('start_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Started')),
                ('time_to_execute', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Executed')),
            ],
        ),
    ]
