# Generated by Django 4.2.1 on 2023-06-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0003_alter_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
