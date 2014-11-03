from django.contrib import admin
from models import Doctor, DoctorContent, DoctorContentType, \
    NotificationEmail


class AdminDoctor(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name',)


class AdminDoctorContent(admin.ModelAdmin):
    pass


class AdminDoctorContentType(admin.ModelAdmin):
    list_display = ('name',)


class AdminNotificationEmail(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Doctor, AdminDoctor)
admin.site.register(DoctorContent, AdminDoctorContent)
admin.site.register(DoctorContentType, AdminDoctorContentType)
admin.site.register(NotificationEmail, AdminNotificationEmail)
