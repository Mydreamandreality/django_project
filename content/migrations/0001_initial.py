# Generated by Django 2.2.1 on 2019-05-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.TextField(primary_key=True, serialize=False, verbose_name='主键pk')),
                ('title', models.TextField(max_length=50, verbose_name='文章标题')),
                ('brief_content', models.TextField(max_length=500, verbose_name='文章摘要')),
                ('article_content', models.TextField(max_length=10000, verbose_name='文章内容')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
    ]