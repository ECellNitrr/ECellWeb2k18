from django.db import models
from appprofile.models import Profile

class Questionset(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    set_no = models.IntegerField()
    meta = models.ImageField(upload_to='staticfiles/uploads/questionset')
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=256)
    description = models.TextField()
    meta = models.ImageField(upload_to='staticfiles/uploads/question')
    time_limit = models.IntegerField()
    score = models.IntegerField()
    q_type = models.IntegerField()
    q_set = models.ForeignKey(Questionset,on_delete=models.CASCADE)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    answer = models.IntegerField()

    def __int__(self):
        return self.answer
