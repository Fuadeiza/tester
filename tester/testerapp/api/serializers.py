from rest_framework import serializers
from testerapp.models import testQuestions


class testQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= testQuestions
        field= '__all__'