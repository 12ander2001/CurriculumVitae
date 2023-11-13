# Generated by Django 4.2.5 on 2023-11-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0003_alter_curriculumvitae_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='education',
        ),
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='workexperience',
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='education',
            field=models.ManyToManyField(to='CurriculumVitae.education'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='interest',
            field=models.ManyToManyField(to='CurriculumVitae.interests'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='skills',
            field=models.ManyToManyField(to='CurriculumVitae.skills'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='workexperience',
            field=models.ManyToManyField(to='CurriculumVitae.workexperience'),
        ),
    ]
