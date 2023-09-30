# Generated by Django 4.1 on 2022-10-08 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0034_alter_subdomain_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='subdomain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.subdomain'),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
