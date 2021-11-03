from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '03_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials'),
        ),
    ]