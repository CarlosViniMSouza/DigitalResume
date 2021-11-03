from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '02_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]