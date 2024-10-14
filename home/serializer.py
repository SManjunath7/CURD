from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        #exclude = ['id']
        fields = ['name','age','id','email']
        #fileds= '__all__'
    