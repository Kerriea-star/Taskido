# Generated by Django 3.2.9 on 2022-06-07 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(default='Tasks', max_length=108, verbose_name='Category')),
                ('completed', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.owner')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task', models.CharField(max_length=89, verbose_name='task')),
                ('completed', models.BooleanField(default=False, verbose_name='completed')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Date due')),
                ('important', models.BooleanField(default=False, verbose_name='important')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='tasks.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.owner')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'ordering': ('-important', 'due_date'),
            },
        ),
    ]
