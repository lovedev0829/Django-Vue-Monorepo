from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from api.core.v1.serializers import NoteSerializer, UserSerializer
from api.models import Note
from api.versions import LegacyAPIVersion

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class NoteViewSet(viewsets.GenericViewSet, 
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    
    versioning_class = LegacyAPIVersion
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
   
    search_fields = ["title", "body"]
    ordering_fields = ["title", "created_at"]
    ordering = ["-created_at"]
    throttle_classes = [UserRateThrottle]
    
    
    @swagger_auto_schema(
        operation_summary="List all notes for the authenticated user",
        operation_description="This endpoint returns a list of notes for the authenticated user.",
        responses={
            status.HTTP_200_OK: openapi.Response("Ok", NoteSerializer(many=True)),
            status.HTTP_204_NO_CONTENT : openapi.Response("No Content"),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("Unauthorized"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        },
        produces = ["application/json", "application/xml", "text/html"]
    )
    def list(self, request, *args, **kwargs):
        try:
            notes = Note.objects.filter(user_id=request.user)

            page = self.paginate_queryset(notes)
            if page is not None:
                serializer = self.get_serializer(page, many=True).data
                return self.get_paginated_response(serializer)

            serializer = self.get_serializer(notes, many=True).data
            
        except:
            return Reponse({"details" : "Internal Server Error"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer, status = status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        operation_summary = "Create a new note for the authenticated user",
        operation_description = "This endpoint allows the authenticated user to create a new note.",
        request_body = NoteSerializer,
        responses = {
            status.HTTP_201_CREATED: openapi.Response("Created", NoteSerializer),
            status.HTTP_400_BAD_REQUEST: openapi.Response('Bad Request'),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("Unauthorized"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        }, 
        consumes = ["application/json"],
        produces = ["application/json", "application/xml", "text/html"],
    )
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            note = serializer.save(user_id=request.user)
            response_data = self.get_serializer(note).data
        
        except: 
            return Response({"details" : "Internal Server Error"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    
    @swagger_auto_schema(
        operation_summary="Retrieve details of a specific note",
        operation_description="This endpoint retrieves details of a specific note for the authenticated user.", 
        responses = {
            status.HTTP_200_OK : openapi.Response("Ok", NoteSerializer()),
            status.HTTP_204_NO_CONTENT : openapi.Response("No Content"),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("Unauthorized"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        },
        produces = ["application/json", "application/xml", "text/html"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_summary="Update details of a specific note",
        operation_description="This endpoint updates details of a specific note for the authenticated user.",
        request_body=NoteSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response("Ok", NoteSerializer()),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("Unauthorized"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        },
        consumes = ["application/json"],
        produces = ["application/json", "application/xml", "text/html"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_summary="Partially update details of a specific note",
        operation_description="This endpoint partially updates details of a specific note for the authenticated user.",
        request_body=NoteSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response("Ok", NoteSerializer()),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("Unauthorized"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        },
        consumes = ["application/json"],
        produces = ["application/json", "application/xml", "text/html"]
    )
    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception = True)
            self.perform_update(serializer)
        except:
            return Response({"details": "Internal Server Error"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        operation_summary="Delete a specific note",
        operation_description="This endpoint deletes a specific note for the authenticated user.",
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response("No Content"),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("Unauthorized"),
            status.HTTP_403_FORBIDDEN: openapi.Response("Forbidden"),
            status.HTTP_500_INTERNAL_SERVER_ERROR : openapi.Response("Internal Server Error")
        },
        produces = ["application/json", "application/xml", "text/html"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)