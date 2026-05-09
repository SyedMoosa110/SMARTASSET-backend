import google.generativeai as genai
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Asset, Assignment, ChatHistory
from .serializers import AssetSerializer, AssignmentSerializer, ChatHistorySerializer

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    @action(detail=True, methods=['post'])
    def support(self, request, pk=None):
        asset = self.get_object()
        user_query = request.data.get('query')

        if not user_query:
            return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Prompt Engineering
        prompt = f"""
        You are a technical support assistant for office hardware.
        Device Details:
        - Model: {asset.asset_model}
        - RAM: {asset.ram}
        - OS: {asset.os}
        - CPU: {asset.cpu}
        
        User Problem: {user_query}
        
        Please provide concise, step-by-step repair steps or troubleshooting advice specifically tailored for this hardware configuration.
        """

        try:
            model = genai.GenerativeModel('gemini-flash-latest')
            response = model.generate_content(prompt)
            ai_response = response.text

            # Store chat history
            ChatHistory.objects.create(
                asset=asset,
                user_query=user_query,
                ai_response=ai_response
            )

            return Response({"response": ai_response})
        except Exception as e:
            print(f"AI Error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ChatHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChatHistory.objects.all()
    serializer_class = ChatHistorySerializer
