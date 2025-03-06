from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:  # Meta should be capitalized
        model = Project
        fields = ('name', 'start_date', 'end_date', 'comments', 'status')
