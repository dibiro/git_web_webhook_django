# Generated by Django 2.2.1 on 2019-05-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('git_name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'projects',
                'db_table': 'project',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_updates', to='command.Project')),
            ],
            options={
                'verbose_name_plural': 'updates',
                'db_table': 'update',
            },
        ),
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Command', models.TextField()),
                ('log', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='command.Update')),
            ],
            options={
                'verbose_name_plural': 'update_items',
                'db_table': 'update_item',
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('command', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('position', models.PositiveIntegerField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='command_projects', to='command.Project')),
            ],
            options={
                'verbose_name_plural': 'commands',
                'db_table': 'command',
            },
        ),
    ]
