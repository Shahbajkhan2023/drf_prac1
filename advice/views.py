from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from .serializers import StudentSerializer

class CourseRecommendationView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Access request attributes
        method = request.method
        content_type = request.content_type
        accepted_renderer = request.accepted_renderer
        accepted_media_type = request.accepted_media_type

        # Parse request data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data
            course = serializer.validated_data['course']
            time_remaining = serializer.validated_data['time_remaining']
            
            # Generate recommendation
            language_recommendation = self.get_language_recommendation(course, time_remaining)
            
            # Create response
            response_data = {
                'recommended_language': language_recommendation,
                'method': method,
                'content_type': content_type,
                'accepted_renderer': str(accepted_renderer),
                'accepted_media_type': accepted_media_type,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_language_recommendation(self, course, time_remaining):
        # Simple recommendation logic
        if time_remaining < 6:
            return "JavaScript"
        elif time_remaining < 12:
            return "Python"
        else:
            return "Java"
