from django.contrib import admin

from users.models import Profile


class AllergyInline(admin.TabularInline):
    model = Profile.allergy.through


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth"]
    inlines = (AllergyInline,)
    exclude = ["allergy"]
