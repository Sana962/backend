from rest_framework import serializers
from .models import Answer, AssignemntSimple

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('text',)

class AssignmentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignemntSimple
        fields = '__all__'