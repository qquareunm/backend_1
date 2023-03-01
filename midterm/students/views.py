from rest_framework import generics
from students.serializer import StudentSerializers
from students.models import Student
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json






@csrf_exempt
def students_handler(request, pk):
    if request.method == 'GET':
        students = Student.objects.all(id=pk)
        serializer = StudentSerializers(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = StudentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe=False)
    

@csrf_exempt
def students_handler(request, pk):
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            students_list = Student.objects.get(id=pk)
            serializer = StudentSerializers(data=data, instance=students_list)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'message': 'Students list not found'}, status=status.HTTP_404_NOT_FOUND, safe=False)



