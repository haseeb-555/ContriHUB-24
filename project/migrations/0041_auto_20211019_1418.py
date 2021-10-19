# Generated by Django 3.2.7 on 2021-10-19 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0040_alter_pullrequest_contributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=56, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_domain', models.CharField(max_length=56, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='domain',
        ),
        migrations.CreateModel(
            name='SubDomainProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('sub_domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.subdomain')),
            ],
        ),
    ]
