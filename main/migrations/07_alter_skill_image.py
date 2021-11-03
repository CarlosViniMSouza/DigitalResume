from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211013_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='skills'),
        ),
    ]