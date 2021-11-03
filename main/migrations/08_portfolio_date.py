from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '07_alter_skill_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]