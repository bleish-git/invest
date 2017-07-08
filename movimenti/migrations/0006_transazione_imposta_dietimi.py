# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimenti', '0005_auto_20150802_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='transazione',
            name='imposta_dietimi',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True),
        ),
    ]
