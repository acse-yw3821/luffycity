# Generated by Django 4.2.4 on 2023-09-30 11:26

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_level_alter_course_attachment_path_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_viedo',
            new_name='course_video',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_cover',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, max_length=255, null=True, upload_to='course/cover', variations={'thumb_1080x608': (1080, 608), 'thumb_108x61': (108, 61, True), 'thumb_540x304': (540, 304)}, verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='avatar',
            field=stdimage.models.StdImageField(force_min_size=False, null=True, upload_to='teacher', variations={'thumb_400x400': (400, 400), 'thumb_50x50': (50, 50, True), 'thumb_800x800': (800, 800)}, verbose_name='讲师头像'),
        ),
    ]