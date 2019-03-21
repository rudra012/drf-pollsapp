from django.db.models import Case, IntegerField, Sum, When
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from tracks.models import Track, Question
from tracks.serializers import QuestionCreateSerializer, TrackCreateSerializer, \
    TrackListSerializer, TrackDetailSerializer, QuestionSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    list:
    API to list all tracks

    retrieve:
    API to get details of tracks and it's questions

    create:
    API to create new track with questions

    Sample data to create new Track
    ```
    {
      "track_title": "My sample track",
      "questions": [
        {"question_txt": "My question1"},
        {"question_txt": "My question2"},
        {"question_txt": "My question3"},
        {"question_txt": "My question4"}
      ]
    }
    ```
    """
    queryset = Track.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TrackCreateSerializer
        elif self.action == 'retrieve':
            return TrackDetailSerializer
        return TrackListSerializer

    def create(self, request, *args, **kwargs):
        # Get Track serializer, validate it and save to DB
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        questions = serializer.validated_data.pop('questions')
        track = serializer.save()

        # Create question data for tracks and validate it
        questions = list(map(lambda question: {'question_txt': question['question_txt'], 'track': track.id},
                             questions))
        # print(questions)
        question_serializer = QuestionCreateSerializer(data=questions, many=True)
        question_serializer.is_valid(raise_exception=True)
        question_serializer.save()
        response = {
            'message': 'Track created successfully'
        }
        return Response(response, status=status.HTTP_201_CREATED)


class QuestionViewSet(viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['get'], pagination_class=LimitOffsetPagination)
    def answer_summary(self, request, pk=None):
        queryset = Question.objects.annotate(
            correct_sum=Sum(Case(When(question_answers__is_correct=True, then=1), output_field=IntegerField()))).values(
            'correct_sum').annotate(
            wrong_sum=Sum(Case(When(question_answers__is_correct=False, then=1), output_field=IntegerField()))).values(
            'id', 'question_txt', 'correct_sum', 'wrong_sum')
        page = self.paginate_queryset(queryset)
        return self.get_paginated_response(page)
