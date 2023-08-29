from django.db import models as django_models


class UserProfile(django_models.Model):
    name = django_models.CharField(max_length=60)
    post = django_models.CharField(max_length=20)
    related_cafe = django_models.ForeignKey('RelatedCafe', on_delete=django_models.CASCADE, null=True)
    email = django_models.EmailField(max_length=254)
    telephone_number = django_models.CharField(max_length=13)

    def __str__(self):
        return self.name


class RelatedCafe(django_models.Model):
    name = django_models.CharField(max_length=20)
    address = django_models.CharField(max_length=100)
    manager_name = django_models.ManyToManyField('UserProfile', blank=True)

    def __str__(self):
        return self.name


class TimeAbilities(django_models.Model):
    user_name = django_models.CharField(max_length=20)
    week = django_models.DateField('Понедельник на неделе')
    monday_1 = django_models.CharField(max_length=20)
    monday_2 = django_models.CharField(max_length=20)
    tuesday_1 = django_models.CharField(max_length=20)
    tuesday_2 = django_models.CharField(max_length=20)
    wednesday_1 = django_models.CharField(max_length=20)
    wednesday_2 = django_models.CharField(max_length=20)
    thursday_1 = django_models.CharField(max_length=20)
    thursday_2 = django_models.CharField(max_length=20)
    friday_1 = django_models.CharField(max_length=20)
    friday_2 = django_models.CharField(max_length=20)
    saturday_1 = django_models.CharField(max_length=20)
    saturday_2 = django_models.CharField(max_length=20)
    sunday_1 = django_models.CharField(max_length=20)
    sunday_2 = django_models.CharField(max_length=20)


class CafeWorkingHours(django_models.Model):
    name = django_models.ForeignKey('RelatedCafe', on_delete=django_models.CASCADE, null=True)
    hour_6_7 = django_models.IntegerField()
    hour_7_8 = django_models.IntegerField()
    hour_8_9 = django_models.IntegerField()
    hour_9_10 = django_models.IntegerField()
    hour_10_11 = django_models.IntegerField()
    hour_11_12 = django_models.IntegerField()
    hour_12_13 = django_models.IntegerField()
    hour_13_14 = django_models.IntegerField()
    hour_14_15 = django_models.IntegerField()
    hour_15_16 = django_models.IntegerField()
    hour_16_17 = django_models.IntegerField()
    hour_17_18 = django_models.IntegerField()
    hour_18_19 = django_models.IntegerField()
    hour_19_20 = django_models.IntegerField()
    hour_20_21 = django_models.IntegerField()
    hour_21_22 = django_models.IntegerField()
    hour_22_23 = django_models.IntegerField()
    hour_23_24 = django_models.IntegerField()


class ScheduleForOneDay(django_models.Model):
    cafe = django_models.CharField(max_length=60, blank=True)
    week = django_models.DateField('Понедельник на неделе')
    day_of_week = django_models.CharField(max_length=10)
    hour_6_7 = django_models.CharField(max_length=60, blank=True)
    hour_7_8 = django_models.CharField(max_length=60, blank=True)
    hour_8_9 = django_models.CharField(max_length=60, blank=True)
    hour_9_10 = django_models.CharField(max_length=60, blank=True)
    hour_10_11 = django_models.CharField(max_length=60, blank=True)
    hour_11_12 = django_models.CharField(max_length=60, blank=True)
    hour_12_13 = django_models.CharField(max_length=60, blank=True)
    hour_13_14 = django_models.CharField(max_length=60, blank=True)
    hour_14_15 = django_models.CharField(max_length=60, blank=True)
    hour_15_16 = django_models.CharField(max_length=60, blank=True)
    hour_16_17 = django_models.CharField(max_length=60, blank=True)
    hour_17_18 = django_models.CharField(max_length=60, blank=True)
    hour_18_19 = django_models.CharField(max_length=60, blank=True)
    hour_19_20 = django_models.CharField(max_length=60, blank=True)
    hour_20_21 = django_models.CharField(max_length=60, blank=True)
    hour_21_22 = django_models.CharField(max_length=60, blank=True)
    hour_22_23 = django_models.CharField(max_length=60, blank=True)
    hour_23_24 = django_models.CharField(max_length=60, blank=True)

    @classmethod
    def create(cls, field_value_dict):
        schedule_for_one_day = cls(cafe=field_value_dict['cafe'], week=field_value_dict['week'],
                                   day_of_week=field_value_dict['day_of_week'],
                                   hour_6_7=field_value_dict['hour_6_7'], hour_7_8=field_value_dict['hour_7_8'],
                                   hour_8_9=field_value_dict['hour_8_9'], hour_9_10=field_value_dict['hour_9_10'],
                                   hour_10_11=field_value_dict['hour_10_11'], hour_11_12=field_value_dict['hour_11_12'],
                                   hour_12_13=field_value_dict['hour_12_13'], hour_13_14=field_value_dict['hour_13_14'],
                                   hour_14_15=field_value_dict['hour_14_15'], hour_15_16=field_value_dict['hour_15_16'],
                                   hour_16_17=field_value_dict['hour_16_17'], hour_17_18=field_value_dict['hour_17_18'],
                                   hour_18_19=field_value_dict['hour_18_19'], hour_19_20=field_value_dict['hour_19_20'],
                                   hour_20_21=field_value_dict['hour_20_21'], hour_21_22=field_value_dict['hour_21_22'],
                                   hour_22_23=field_value_dict['hour_22_23'], hour_23_24=field_value_dict['hour_23_24'])
        return schedule_for_one_day
