# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 07:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_village', models.CharField(blank=True, max_length=255, null=True)),
                ('postoffice', models.CharField(blank=True, max_length=255, null=True)),
                ('post_code', models.CharField(blank=True, max_length=255, null=True)),
                ('flat_no', models.CharField(blank=True, max_length=255, null=True)),
                ('police_station_thana', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('address_type', models.CharField(blank=True, choices=[('present', 'present'), ('permanent', 'permanent')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('otherother', 'other')], max_length=32)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaryAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_offence', models.CharField(blank=True, max_length=255, null=True)),
                ('punishment', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_institution', models.CharField(blank=True, max_length=255, null=True)),
                ('principals_subject', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=32)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('nationalid', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True)),
                ('name_spouse', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=512, null=True)),
                ('longitude', models.CharField(blank=True, max_length=512, null=True)),
                ('fathers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mothers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('home_district', models.CharField(blank=True, max_length=255, null=True)),
                ('is_freedomfighter', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=32)),
                ('spouse_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_district', models.CharField(blank=True, max_length=255, null=True)),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('date_joining', models.DateField(blank=True, null=True)),
                ('entry_designation', models.CharField(blank=True, max_length=255, null=True)),
                ('entry_scale', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
                ('archive_status', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=32)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=32)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee_Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('no_of_units_completed', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('units_points', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('date_achivement', models.DateField(blank=True, null=True)),
                ('points_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ManagerAchievement', to='hr.Employee')),
                ('points_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeAchievement', to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('read', models.CharField(blank=True, max_length=255, null=True)),
                ('write', models.CharField(blank=True, max_length=255, null=True)),
                ('speak', models.CharField(blank=True, max_length=255, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Languages', to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_promotion', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('pay_scale', models.CharField(blank=True, max_length=255, null=True)),
                ('nature_promotion', models.CharField(blank=True, max_length=255, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Promotions', to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Rest_of_recreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(blank=True, null=True)),
                ('coming_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Rest_of_recreation', to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Retirement_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Retirement_year', to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('office_name', models.CharField(blank=True, max_length=255, null=True)),
                ('section', models.CharField(blank=True, max_length=255, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ServiceHistory', to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_trainin', models.CharField(blank=True, max_length=255, null=True)),
                ('institution', models.CharField(blank=True, max_length=255, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('trining_type', models.CharField(blank=True, choices=[('local', 'local'), ('foreign', 'foreign')], max_length=32)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Training', to='hr.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Education', to='hr.Employee'),
        ),
        migrations.AddField(
            model_name='district',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='District', to='hr.Employee'),
        ),
        migrations.AddField(
            model_name='disciplinaryaction',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DisciplinaryAction', to='hr.Employee'),
        ),
        migrations.AddField(
            model_name='children',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Children', to='hr.Employee'),
        ),
        migrations.AddField(
            model_name='address',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Address', to='hr.Employee'),
        ),
    ]
