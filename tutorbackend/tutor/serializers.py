from rest_framework import serializers
from .models import TutorModel

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorModel
        fields = '__all__'

    # def create(self, validated_data):
    #     tutorial = TutorModel(
    #         question = validated_data['question'],
    #         answer = validated_data['answer'],
    #         date_create = validated_data['date_create'],
    #         category = validated_data['category'],
    #         topic = validated_data['topic'],
    #         student_name = validated_data['student_name'],
    #         company = validated_data['company'],
    #         links = validated_data['links'],
    #     )
    #     tutorial.save()
    #     return tutorial
