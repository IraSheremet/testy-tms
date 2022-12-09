# Generated by Django 3.2 on 2022-11-28 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils
import validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0002_project_is_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('file_extension', models.CharField(max_length=255)),
                ('size', models.PositiveBigIntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True)),
                ('file', models.FileField(max_length=150, upload_to=utils.get_attachments_file_path, validators=[validators.ExtensionValidator()])),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', validators=[validators.ProjectValidator()])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]