from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Answer, AssignemntSimple
from .serializers import AnswerSerializer, AssignmentSimpleSerializer


# Create your views here.

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AssignmentSimpleView(viewsets.ViewSet):

    def post(self, request):
        # queryset = AssignemntSimple.objects.all()
        serializer_class = AssignmentSimpleSerializer(data=request.data)
        serializer_class.save()
        return Response(serializer_class.data)
