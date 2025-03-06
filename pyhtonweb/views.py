from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class projectviewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # The list method is already handled by ModelViewSet,
    # but you can override it if needed.
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    # Create a new project
    def create(self, request):
        # You can use the `serializer` to validate and save the data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created status
        return Response(serializer.errors, status=400)  # Bad request status

    # Retrieve a single project by primary key
    def retrieve(self, request, pk=None):
        project = self.get_object()  # get_object is provided by ModelViewSet
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    # Update an existing project by primary key
    def update(self, request, pk=None):
        project = self.get_object()  # get_object is provided by ModelViewSet
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # Delete a project by primary key
    def destroy(self, request, pk=None):
        project = self.get_object()  # get_object is provided by ModelViewSet
        project.delete()
        return Response(status=204)  # No content, since we deleted the object
