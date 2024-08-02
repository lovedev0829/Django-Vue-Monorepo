from django.contrib.admin import ModelAdmin


class NoteAdmin(ModelAdmin):
    
    list_display = ["title", "created_at", "updated_at"]
    readonly_fields = ("created_at", "updated_at")