# Generated by Django 4.0.3 on 2022-04-06 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag')),
            ],
        ),
    ]
