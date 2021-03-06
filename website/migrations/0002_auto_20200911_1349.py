# Generated by Django 3.1.1 on 2020-09-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Type name', max_length=200)),
                ('phone', models.IntegerField(help_text='Type phone')),
                ('email', models.EmailField(help_text='Type email', max_length=254, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
