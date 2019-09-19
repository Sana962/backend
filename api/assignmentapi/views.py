from rest_framework import viewsets
from rest_framework.response import Response
from .models import Answer, AssignemntSimple
from .serializers import AnswerSerializer, AssignmentSimpleSerializer
from django.http import JsonResponse
import json

# Create your views here.

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


# class AssignmentSimpleView(viewsets.ModelViewSet):
#     queryset = AssignemntSimple.objects.all()
#     serializer_class = AssignmentSimpleSerializer
#     # queryset = AssignemntSimple.objects.all()
#     # serializer_class = AssignmentSimpleSerializer(data=request.data)
#     # serializer_class.save()
#     # return Response(serializer_class.data)

class AssignmentSimpleView(viewsets.ViewSet):
    @staticmethod
    def create(request):
        decoded = request.body.decode('utf8').replace("'", '"')
        obj = json.loads(decoded)
        #print(obj.get("query"))
        from .testimport import Word2Vec
        test_import = Word2Vec(obj.get("query"), obj.get("template"))
        final_response = test_import.loadFormat()
        return Response(final_response)
        # return JsonResponse(request.body, safe=False)
        # serializer_class = AssignmentSimpleSerializer(AssignmentSimpleView, data=request.body)
        # if serializer_class.is_valid():
        #     serializer_class.save()
        #     return Response(serializer_class.data)
        # return Response('Invalid Format')

    # def getAnswer(self, request):
    #     return Response()

    # @staticmethod
    # def list(request):
    #     queryset = AssignemntSimple.objects.all()
    #     serializer_class = AssignmentSimpleSerializer(queryset, many=True)
    #     return Response(serializer_class.data)
    #     # queryset = AssignemntSimple.objects.all()
    #     # serializer_class = AssignmentSimpleSerializer(data=request.data)
    #     # serializer_class.save()
    #     # return Response(serializer_class.data)
