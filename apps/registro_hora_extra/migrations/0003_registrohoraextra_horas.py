# Generated by Django 5.0 on 2024-01-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, help_text='horas trabalhadas', max_digits=5),
            preserve_default=False,
        ),
    ]
