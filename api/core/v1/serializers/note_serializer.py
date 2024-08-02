from rest_framework import serializers
from api.models import Note
import bleach 

class NoteSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    word_count = serializers.SerializerMethodField(method_name = "count_words")
    
    class Meta:
        
        model = Note
        fields = ["id", "title", "body", "user", "word_count"]
        read_only_fields = ("created_at", "updated_at")
        unique_together = ("title")
        
    
    def validate(self, attrs):

        if "title" in attrs:
            attrs["title"] = bleach.clean(attrs["title"])

        if "body" in attrs:
            attrs["body"] = bleach.clean(attrs["body"])

        return super().validate(attrs)
    
    
    def get_user(self, instance):
        
        if instance:
            user_instance = instance.user_id
            return  {
                "id" : user_instance.id,
                "username" : user_instance.username,
                "email" : user_instance.email
            }
        else:
            return None
    
    
    def to_representation(self, instance):
        
        data = super().to_representation(instance)
        data["user"] = self.get_user(instance)
        return data
    
    
    def count_words(self, note : Note):
        return len(note.body.split(" "))
        