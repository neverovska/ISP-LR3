# Generated by Django 3.0.7 on 2022-06-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(db_index=True, default='', max_length=100)),
                ('item_id', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('quantity', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
