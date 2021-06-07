# Generated by Django 3.1.3 on 2021-02-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='problem',
            name='answer',
            field=models.CharField(choices=[('A', '选项A'), ('B', '选项B'), ('C', '选项C'), ('D', '选项D')], max_length=1024, verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
    ]