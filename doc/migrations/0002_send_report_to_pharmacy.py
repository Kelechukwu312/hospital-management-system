# Generated by Django 2.2.6 on 2020-07-20 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_pham_model_category'),
        ('doc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_report_to_pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=120)),
                ('Time', models.CharField(max_length=300)),
                ('Pham', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pham', to='user.Pham_model')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.patients')),
            ],
        ),
    ]
