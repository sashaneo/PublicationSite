# Generated by Django 3.1.1 on 2020-09-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200918_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='link',
            field=models.CharField(default=1, help_text='Type link', max_length=150),
            preserve_default=False,
        ),
    ]