from django.contrib import admin
from .models import UserProfile, RelatedCafe, TimeAbilities, CafeWorkingHours, ScheduleForOneDay


admin.site.register(UserProfile)
admin.site.register(RelatedCafe)
admin.site.register(TimeAbilities)
admin.site.register(CafeWorkingHours)
admin.site.register(ScheduleForOneDay)