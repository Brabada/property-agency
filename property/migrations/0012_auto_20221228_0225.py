# Generated by Django 2.2.24 on 2022-12-27 23:25

from django.db import migrations


def migrate_owners_from_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            defaults={
                'normalized_phonenumber': flat.owner_pure_phone,
            },
        )



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(migrate_owners_from_flats)
    ]