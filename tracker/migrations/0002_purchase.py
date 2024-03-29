# Generated by Django 3.2 on 2021-04-07 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date_purchased', models.DateField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.item')),
            ],
        ),
    ]
