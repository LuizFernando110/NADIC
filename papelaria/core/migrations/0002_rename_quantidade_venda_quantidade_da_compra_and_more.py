# Generated by Django 5.0.4 on 2024-04-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='quantidade',
            new_name='quantidade_da_compra',
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade_em_estoque',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
