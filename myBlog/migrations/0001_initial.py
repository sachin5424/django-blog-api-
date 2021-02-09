# Generated by Django 3.1.6 on 2021-02-07 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BLOG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='media/Blog')),
                ('Active', models.BooleanField(default=False)),
                ('Featured', models.BooleanField(default=False)),
                ('Description', models.TextField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myBlog.categories')),
            ],
        ),
    ]
