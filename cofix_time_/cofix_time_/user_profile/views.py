from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import datetime
import sqlite3

from .models import UserProfile, RelatedCafe, TimeAbilities, CafeWorkingHours, ScheduleForOneDay
from .forms import TimeAbilitiesForm, WeekChoosingForm


def user_profile(request):
    pk = request.session.get('user_id')
    profile_information = UserProfile.objects.get(pk=pk)
    user = User.objects.get(pk=pk)
    context = {
        'profile_information': profile_information,
        'user': user,
    }
    return render(request, 'user_profile.html', context)


def time_abilities(request):
    pk = request.session.get('user_id')
    profile_information = UserProfile.objects.get(pk=pk)
    today_date = datetime.date.today()
    abilities = TimeAbilities.objects.all()
    user = User.objects.get(pk=pk)

    weeks_values = TimeAbilities.objects.values('week')
    weeks_back = list()
    for week_dict in weeks_values:
        week_list = week_dict.values()
        for value in week_list:
            weeks_back.append(value)
    weeks_back = sorted(list(set(weeks_back)), reverse=True)
    weeks = weeks_back

    form = TimeAbilitiesForm()
    if request.method == 'POST':
        form = TimeAbilitiesForm(request.POST)
        if form.is_valid():
            try:
                user_prier_time_abilities = TimeAbilities.objects.get(user_name=profile_information.name)
                weeks_prier = user_prier_time_abilities.week
                last_ability = max(weeks_prier)
            except Exception:
                last_ability = today_date
            if last_ability <= today_date:
                time_ability = TimeAbilities(
                    user_name=profile_information.name,
                    week=form.cleaned_data['week'],
                    monday_1=form.cleaned_data['monday_1'],
                    monday_2=form.cleaned_data['monday_2'],
                    tuesday_1=form.cleaned_data['tuesday_1'],
                    tuesday_2=form.cleaned_data['tuesday_2'],
                    wednesday_1=form.cleaned_data['wednesday_1'],
                    wednesday_2=form.cleaned_data['wednesday_2'],
                    thursday_1=form.cleaned_data['thursday_1'],
                    thursday_2=form.cleaned_data['thursday_2'],
                    friday_1=form.cleaned_data['friday_1'],
                    friday_2=form.cleaned_data['friday_2'],
                    saturday_1=form.cleaned_data['saturday_1'],
                    saturday_2=form.cleaned_data['saturday_2'],
                    sunday_1=form.cleaned_data['sunday_1'],
                    sunday_2=form.cleaned_data['sunday_2'],
                )
                time_ability.save()
                messages.success(request, mark_safe('Ваши временные возможности отправлены'))
            else:
                messages.info(request, mark_safe('Эта информация уже была отправлена ранее'))

    context = {
        'user': user,
        'form': form,
        'today_date': today_date,
        'profile_information': profile_information,
        'abilities': abilities,
        'weeks': weeks
    }
    return render(request, 'time_abilities.html', context)


def stuff(request):
    pk = request.session.get('user_id')
    profile_information = UserProfile.objects.get(pk=pk)
    employees = UserProfile.objects.all()
    user = User.objects.get(pk=pk)
    context = {
        'profile_information': profile_information,
        'employees': employees,
        'user': user,
    }
    return render(request, 'stuff.html', context)


def schedule(request):
    pk = request.session.get('user_id')
    profile_information = UserProfile.objects.get(pk=pk)
    user = User.objects.get(pk=pk)
    today_date = datetime.date.today()
    try:
        schedule_weeks_list = ScheduleForOneDay.objects.values('week')
        schedule_weeks = set()
        for week_dict in schedule_weeks_list:
            schedule_weeks.add(week_dict['week'])
        last_schedule_week = sorted(list(schedule_weeks), reverse=True)[0]
        last_schedules = []
        ids = list(CafeWorkingHours.objects.values_list('name', flat=True))
        for id in ids:
            print(id)
            day_info = CafeWorkingHours.objects.values().get(name=id)
            print(day_info['name_id'])
            last_schedule = ScheduleForOneDay.objects.filter(cafe=day_info['name_id'], week=last_schedule_week)
            print(last_schedule)
            last_schedules.append(last_schedule)
        print(last_schedules)
    except Exception:
        last_schedule_week = 'Нет созданных расписаний'
        last_schedules = 'Нет созданных расписаний'

    context = {
        'profile_information': profile_information,
        'user': user,
        'last_schedule_week': last_schedule_week,
        'last_schedules': last_schedules,
        'today_date': today_date
    }
    return render(request, 'schedule.html', context)


def cafes(request):
    pk = request.session.get('user_id')
    all_cafes = RelatedCafe.objects.all()
    user_information = UserProfile.objects.get(pk=pk)
    rel_cafe_name = user_information.related_cafe
    rel_cafe_information = RelatedCafe.objects.get(name=rel_cafe_name)
    manager_information = UserProfile.objects.get(post='UK')
    working_hours = CafeWorkingHours.objects.all()
    user = User.objects.get(pk=pk)
    context = {
        'all_cafes': all_cafes,
        'rel_cafe_information': rel_cafe_information,
        'user_information': user_information,
        'user': user,
        'manager_information': manager_information,
        'working_hours': working_hours,
    }
    return render(request, 'cafes.html', context)


def schedule_making(request):
    form = WeekChoosingForm()
    if request.method == 'POST':
        form = WeekChoosingForm(request.POST)
        if form.is_valid():
            week = form.cleaned_data.get('week')

            list_of_days = ['monday_1', 'tuesday_1', 'wednesday_1', 'thursday_1', 'friday_1', 'saturday_1', 'sunday_1']
            list_of_days_end = ['monday_2', 'tuesday_2', 'wednesday_2', 'thursday_2', 'friday_2', 'saturday_2',
                                'sunday_2']

            obj = CafeWorkingHours()
            fields = [(field.name) for field in obj._meta.fields]
            fields = fields[2::]
            hours = []
            for name in fields:
                list_name = name.split('_')
                hours.append(int(list_name[1]))
            hours_dict = dict(zip(hours, fields))

            ids = list(CafeWorkingHours.objects.values_list('id', flat=True))
            for id in ids:
                day_info = CafeWorkingHours.objects.values().get(id=id)
                for day_ in list_of_days:

                    obj = ScheduleForOneDay()
                    fields = [(field.name) for field in obj._meta.fields]
                    first_part = fields[:3:]
                    one_day_schedule_first_part = dict.fromkeys(first_part, None)
                    second_part = fields[3::]
                    one_day_schedule_second_part = dict.fromkeys(second_part, set())
                    one_day_schedule = one_day_schedule_first_part | one_day_schedule_second_part

                    one_day_schedule['week'] = week
                    one_day_schedule['cafe'] = day_info['name_id']
                    one_day_schedule['day_of_week'] = day_[:-2:]

                    employees = UserProfile.objects.filter(post__in=['SS', 'Barista'],
                                                           related_cafe=day_info['name_id'])

                    for employee in employees:
                        try:
                            time_abilities_ = TimeAbilities.objects.values().get(week=week,
                                                                                 user_name=employee.name)
                            try:
                                hour_ = int(time_abilities_[day_])
                                hour_name = hours_dict[hour_]
                                if hour_ in hours and day_info[hour_name] != 0:
                                    day_end = list_of_days_end[list_of_days.index(day_)]
                                    hour_ = int(time_abilities_[day_])
                                    hour_end = int(time_abilities_[day_end])
                                    while hour_end != hour_:
                                        one_day_schedule[hour_name].add(time_abilities_['user_name'])
                                        hour_ += 1
                            except ValueError:
                                pass
                        except Exception:
                            pass
                    print(6)
                    schedule_for_one_day = ScheduleForOneDay.create(one_day_schedule)
                    schedule_for_one_day.save()
            return redirect('schedule')
    else:
        return render(request, 'schedule_making.html', {'form': form})
