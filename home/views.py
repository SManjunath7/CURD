from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):
    courses = {
        'course1': 'python',
        'learn': ['django', 'flask'],
        'course_provide': 'Scalar'
    }
    student = {
        'name': 'shubham',
        'age': 22,
        'place': 'pune'
    }
    name = {
        'name': 'Nagendra',
        'age': 32,
        'place': 'goa'
    }
    birthday = {
        'name': 'Aditya',
        'age': 23,
        'DOB': '11-12-2000'
    }

    if request.method == 'GET':
        print('you hit a get method')
        return Response(courses)
    elif request.method == 'POST':
        print('you hit a post method')
        data = request.data
        print('****')
        print(data)
        print('****')
        return Response(student)
    elif request.method == 'PUT':
        print('you hit a put method')
        return Response(name)
    elif request.method == 'PATCH':
        print('you hit a patch method')
        return Response(birthday)


@api_view(['GET', 'POST','PUT','PATCH','DELETE'])
def person_view(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({"message":"person is deleated"})
    
