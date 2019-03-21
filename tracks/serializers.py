from rest_framework import serializers

from tracks.models import Question, Track


class QuestionCreateSerializer(serializers.ModelSerializer):
    """
    Create question model directly
    """

    class Meta:
        model = Question
        fields = ('track', 'question_txt',)


class QuestionSerializer(serializers.ModelSerializer):
    """
    Get question_txt text from user to create Track model
    """

    class Meta:
        model = Question
        fields = ('id', 'question_txt',)


class TrackCreateSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Track
        fields = ('track_title', 'questions')


class TrackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'track_title')


class TrackDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ('id', 'track_title', 'questions')

    def get_questions(self, obj):
        return QuestionSerializer(obj.track_questions.all(), many=True).data
