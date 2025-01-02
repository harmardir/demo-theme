# Generated by Django 3.2.16 on 2023-02-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0013_auto_20200115_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemode',
            name='android_sku',
            field=models.CharField(blank=True, help_text='OPTIONAL: This is the Android SKU registered on play store for this mode of the course. Leave this blank if the course has not yet been migrated to the ecommerce service.', max_length=255, null=True, verbose_name='Android SKU'),
        ),
        migrations.AddField(
            model_name='coursemode',
            name='ios_sku',
            field=models.CharField(blank=True, help_text='OPTIONAL: This is the iOS SKU registered on app store for this mode of the course.  Leave this blank if the course has not yet been migrated to the ecommerce service.', max_length=255, null=True, verbose_name='iOS SKU'),
        ),
        migrations.AddField(
            model_name='historicalcoursemode',
            name='android_sku',
            field=models.CharField(blank=True, help_text='OPTIONAL: This is the Android SKU registered on play store for this mode of the course. Leave this blank if the course has not yet been migrated to the ecommerce service.', max_length=255, null=True, verbose_name='Android SKU'),
        ),
        migrations.AddField(
            model_name='historicalcoursemode',
            name='ios_sku',
            field=models.CharField(blank=True, help_text='OPTIONAL: This is the iOS SKU registered on app store for this mode of the course.  Leave this blank if the course has not yet been migrated to the ecommerce service.', max_length=255, null=True, verbose_name='iOS SKU'),
        ),
    ]