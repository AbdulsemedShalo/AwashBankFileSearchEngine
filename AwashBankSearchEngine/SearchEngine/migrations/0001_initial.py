# Generated by Django 4.1.2 on 2022-10-10 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileAndDocumentBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileCategory', models.CharField(max_length=100)),
                ('fileContent', models.FileField(upload_to='')),
                ('publicaitonDate', models.DateTimeField(verbose_name='Publication Date')),
                ('publishedBy', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationDate', models.DateTimeField()),
                ('categoryTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='SearchEngine.fileanddocumentbase')),
            ],
        ),
    ]
