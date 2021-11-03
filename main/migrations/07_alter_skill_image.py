from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '06_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='skills'),
        ),
    ]