from rest_framework import serializers

from .import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
        
      
class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = (
            'step_text'
        )

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = (
            'text'
        )


class ReceipeSerializer(serializers.ModelSerializer):
    steps=serializers.StringRelatedField(many=True)
    ingredients=serializers.StringRelatedField(many=True)
    users= UserSerializer(many=False,read_only=True)

    class Meta:
        model = models.Recipe
        fields = (
            'name'
        )

        
    
