# Generated by Django 3.0.5 on 2021-07-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_auto_20210717_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='patientCondition',
            new_name='coginitiveImpairment',
        ),
        migrations.RenameField(
            model_name='referral',
            old_name='referFrom',
            new_name='focalPoint',
        ),
        migrations.RenameField(
            model_name='referral',
            old_name='referTo',
            new_name='foculPoint1',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='doctorId',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='history',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='kin',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='status',
        ),
        migrations.AddField(
            model_name='referral',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='followupRequirements',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='mobility',
            field=models.CharField(choices=[('Bed Bound', 'Bed Bound'), ('Wheelchair', 'Wheelchair'), ('Crutches', 'Crutches'), ('Walking Frame', 'Walking Frame'), ('Requires Assistance', 'Requires Assistance'), ('Independent', 'Independent')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='otherDiagnose',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='patientAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='precautions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='primaryDiagnose',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referralAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referralEmail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referralPhone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referralReason',
            field=models.CharField(choices=[('Inpatient', 'Inpatient'), ('OutPatient', 'OutPatient'), ('Community', 'Communnity')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referralTo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referringAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referringEmail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referringFrom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referringPhone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='selfCare',
            field=models.CharField(choices=[('Carer Dependent', 'Carer Dependent'), ('Requires Commode', 'Requires Commode'), ('Requires Modified Washroom', 'Requires Modified Washroom'), ('Independent', 'Independent')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='transportationNeeds',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='treatments',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Stopped', 'Stopped')], default='Ongoing', max_length=100, null=True),
        ),
    ]
