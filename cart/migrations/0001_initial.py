# Generated by Django 2.2.5 on 2021-08-04 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsid', models.PositiveIntegerField()),
                ('colorid', models.PositiveIntegerField()),
                ('sizeid', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('isdelete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.UserInfo')),
            ],
            options={
                'unique_together': {('goodsid', 'colorid', 'sizeid')},
            },
        ),
    ]