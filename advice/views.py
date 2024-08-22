from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student


class StudentListView(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        
        # Create a response with serialized data
        response_data = {
            'students': serializer.data,
            'method': request.method,
            'content_type': request.content_type,
            'accepted_renderer': str(request.accepted_renderer),
            'accepted_media_type': request.accepted_media_type,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class StudentDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student)
        
        # Include additional context and attributes
        renderer_context = {
            'request': request,
            'format': format,
        }
        response_data = {
            'student': serializer.data,
            'method': request.method,
            'content_type': request.content_type,
            'accepted_renderer': str(request.accepted_renderer),
            'accepted_media_type': request.accepted_media_type,
        }
        
        return Response(
            data=response_data,
            status=status.HTTP_200_OK,
            template_name='myapp/student_detail.html',
            headers={'Custom-Header': 'Value'},
            content_type='application/json'
        )