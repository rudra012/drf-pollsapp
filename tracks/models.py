from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Track(BaseModel):
    track_title = models.CharField(max_length=255)

    def __str__(self):
        return self.track_title


class Question(BaseModel):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='track_questions')
    question_txt = models.TextField()

    def __str__(self):
        return self.question_txt


class Answers(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    is_correct = models.BooleanField(default=False, help_text='Whether')

    def __str__(self):
        return self.question.question_txt
