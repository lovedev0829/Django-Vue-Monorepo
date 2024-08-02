from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    
    
    def get_fieldsets(self, request, obj = None):
        
        fieldsets = super().get_fieldsets(request, obj)[2:]
        
        new_fieldsets = (
            (None, {"fields": ("username", "email", "password")}),
            ("Personal info", {"fields": ("first_name", "middle_name", "last_name")}),
        )
        
        return new_fieldsets + fieldsets
    