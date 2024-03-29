# Generated by Django 5.0.1 on 2024-02-01 06:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vle_name', models.CharField(max_length=50)),
                ('customer_name_on_pan', models.CharField(max_length=50)),
                ('father_name_or_spouse_name', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('address_on_aadhar', models.CharField(max_length=50)),
                ('is_mobile_no_linked_to_aadhar', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppCustomer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('550e8400-e29b-41d4-a716-446655440000'), editable=False)),
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id_version', models.IntegerField()),
                ('customer_name', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField()),
                ('relationship_manager', models.CharField(max_length=50)),
                ('relationship_manager_mobile_no', models.IntegerField()),
                ('customer_onboarded', models.CharField(choices=[('Yes', 'Yes'), ('YES', 'No')], default=True, max_length=3)),
                ('cluster_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
                ('mother_tongue', models.CharField(max_length=50)),
                ('bridge_language', models.CharField(max_length=50)),
                ('customer_name_in_mothertongue', models.CharField(max_length=50)),
                ('calling_name_in_mothertongue', models.CharField(max_length=50)),
                ('calling_name_in_english', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppOnBoarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=8)),
                ('Language_selected', models.CharField(max_length=20)),
                ('pin_code', models.CharField(help_text='Enter your postal code', max_length=10)),
                ('state', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppInsuranceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_insurance', models.IntegerField()),
                ('policy_no_of_Insurance', models.CharField(max_length=50)),
                ('saswat_loan_number', models.IntegerField()),
                ('loan_from', models.CharField(max_length=50)),
                ('Insurance_from', models.CharField(max_length=50)),
                ('insured_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('No_of_cattle', models.IntegerField()),
                ('insured_date', models.DateField()),
                ('insurance_validity_date', models.DateField()),
                ('Insurance_type', models.CharField(max_length=100)),
                ('insurance_status_active', models.BooleanField(default=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saswat_cust_app.whatsappcustomer')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppProspectInfo',
            fields=[
                ('uuid', models.IntegerField()),
                ('prospect_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_no_NBFC', models.CharField(max_length=50)),
                ('loan_from', models.CharField(max_length=50)),
                ('loan_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saswat_cust_app.whatsappcustomer')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppLoanInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_loan', models.IntegerField()),
                ('saswat_loan_number', models.IntegerField()),
                ('loan_no_NBFC', models.CharField(max_length=50)),
                ('loan_from', models.CharField(max_length=50)),
                ('loan_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emi_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emi_date', models.DateField()),
                ('balance_loan_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_type', models.CharField(max_length=50)),
                ('loan_status_active', models.BooleanField(default=True)),
                ('total_no_installment', models.IntegerField()),
                ('no_installment_paid', models.IntegerField()),
                ('overdue_installment', models.IntegerField()),
                ('overdue_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('penalty_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saswat_cust_app.whatsappcustomer')),
                ('prospect_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saswat_cust_app.whatsappprospectinfo')),
            ],
        ),
    ]
