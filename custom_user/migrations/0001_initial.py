# Generated by Django 4.1 on 2023-04-12 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('password', models.CharField(max_length=128)),
                ('salt', models.CharField(blank=True, max_length=255, null=True)),
                ('nickname', models.CharField(max_length=30, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_users', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('last_update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_users', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='System_Settings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('password_settings', models.JSONField(default=dict)),
                ('email_settings', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='User_Settings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('notification_preferences', models.JSONField(default=dict)),
                ('privacy_settings', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=7)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
