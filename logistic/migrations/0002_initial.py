# Generated by Django 4.2.4 on 2023-09-11 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("logistic", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogFeatures",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("NAME_CUSTOMER", models.CharField(max_length=100)),
                ("AGE", models.FloatField()),
                ("CHILDREN", models.FloatField()),
                ("PERS_H", models.FloatField()),
                ("TMADD", models.FloatField()),
                ("TMJOB1", models.FloatField()),
                ("TEL", models.FloatField()),
                ("NMBLOAN", models.FloatField()),
                ("FINLOAN", models.FloatField()),
                ("INCOME", models.FloatField()),
                ("EC_CARD", models.FloatField()),
                ("INC", models.FloatField()),
                ("INC1", models.FloatField()),
                ("BUREAU", models.FloatField()),
                ("LOCATION", models.FloatField()),
                ("LOANS", models.FloatField()),
                ("REGN", models.FloatField()),
                ("DIV", models.FloatField()),
                ("CASH", models.FloatField()),
                (
                    "TITLE",
                    models.CharField(
                        choices=[("", "---------"), ("H", "H"), ("R", "R")],
                        max_length=20,
                    ),
                ),
                (
                    "STATUS",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("V", "V"),
                            ("U", "U"),
                            ("G", "G"),
                            ("E", "E"),
                            ("T", "T"),
                            ("W", "W"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "PRODUCT",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("Radio_TV_Hifi", "Radio_TV_Hifi"),
                            ("Furniture_Carpet", "Furniture_Carpet"),
                            ("Dept_Store_Mail", "Dept_Store_Mail"),
                            ("Leisure", "Leisure"),
                            ("Cars", "Cars"),
                            ("OT", "OT"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "RESID",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("Lease", "Lease"),
                            ("Owner", "Owner"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "NAT",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("German", "German"),
                            ("Turkish", "Turkish"),
                            ("RS", "RS"),
                            ("Greek", "Greek"),
                            ("Yugoslav", "Yugoslav"),
                            ("Italian", "Italian"),
                            ("Other_European", "Other_European"),
                            ("Spanish_Portugue", "Spanish_Portugue"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "PROF",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("Others", "Others"),
                            ("Civil_Service_M", "Civil_Service_M"),
                            ("Self_employed_pe", "Self_employed_pe"),
                            ("Food_Building_Ca", "Food_Building_Ca"),
                            ("Chemical_Industr", "Chemical_Industr"),
                            ("Pensioner", "Pensioner"),
                            ("Sea_Vojage_Gast", "Sea_Vojage_Gast"),
                            ("State_Steel_Ind,", "State_Steel_Ind,"),
                            ("Military_Service", "Military_Service"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "CAR",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("Car", "Car"),
                            ("Without_Vehicle", "Without_Vehicle"),
                            ("Car_and_Motor_bi", "Car_and_Motor_bi"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "CARDS",
                    models.CharField(
                        choices=[
                            ("", "---------"),
                            ("Cheque_card", "Cheque_card"),
                            ("no_credit_cards", "no_credit_cards"),
                            ("Mastercard_Euroc", "Mastercard_Euroc"),
                            ("VISA_mybank", "VISA_mybank"),
                            ("VISA_Others", "VISA_Others"),
                            ("Other_credit_car", "Other_credit_car"),
                            ("American_Express", "American_Express"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Probability",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("probability", models.CharField(max_length=20, null=True)),
                ("default", models.CharField(max_length=20, null=True)),
                (
                    "log_features_key",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="probability",
                        to="logistic.logfeatures",
                    ),
                ),
            ],
        ),
    ]
