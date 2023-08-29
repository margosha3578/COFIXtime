from django import forms


class TimeAbilitiesForm(forms.Form):
    week = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    monday_1 = forms.CharField(label='Понедельник с ', max_length=20)
    monday_2 = forms.CharField(label='Понедельник до ', max_length=20)
    tuesday_1 = forms.CharField(label='Вторник с ', max_length=20)
    tuesday_2 = forms.CharField(label='Вторник до ', max_length=20)
    wednesday_1 = forms.CharField(label='Среда с ', max_length=20)
    wednesday_2 = forms.CharField(label='Среда до ', max_length=20)
    thursday_1 = forms.CharField(label='Четверг с ', max_length=20)
    thursday_2 = forms.CharField(label='Четверг до ', max_length=20)
    friday_1 = forms.CharField(label='Пятница с ', max_length=20)
    friday_2 = forms.CharField(label='Пятница до ', max_length=20)
    saturday_1 = forms.CharField(label='Суббота с ', max_length=20)
    saturday_2 = forms.CharField(label='Суббота до ', max_length=20)
    sunday_1 = forms.CharField(label='Воскресенье с ', max_length=20)
    sunday_2 = forms.CharField(label='Воскресенье до ', max_length=20)


class WeekChoosingForm(forms.Form):
    week = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
