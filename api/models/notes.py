from django.db import models


class Note(models.Model):
    
    user_id = models.ForeignKey("User", on_delete = models.CASCADE, blank = False)
    
    title = models.CharField(max_length = 100, unique = True, blank = False)
    body = models.TextField(blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)    

    REQUIRED_FIELDS = ["title"]
    
    
    class Meta:
        
        ordering = ["-created_at", "-updated_at"]

    
    def __str__(self):
        return self.title
    
    