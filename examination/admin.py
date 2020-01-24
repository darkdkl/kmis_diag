from django.contrib import admin

from examination.models import Diagnostics, Device, Result


admin.site.register(Device)
admin.site.register(Result)


class ResultInline(admin.StackedInline):
    model = Result
    extra = 0


@admin.register(Diagnostics)
class DiagnosticsAdmin(admin.ModelAdmin):
    inlines = [ResultInline]
