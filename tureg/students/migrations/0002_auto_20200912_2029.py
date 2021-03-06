# Generated by Django 3.1.1 on 2020-09-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='status',
        ),
        migrations.DeleteModel(
            name='Quota',
        ),
        migrations.AddField(
            model_name='mycourse',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='course', to='students.Subject'),
        ),
    ]
