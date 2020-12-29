from django.db import models

class Personality(models.Model):
    personality_text   = models.CharField(max_length=100)
    personality_letter = models.CharField(max_length=5, default = '-')
    personality_desc   = models.CharField(max_length=1000)
    # Males  (9, 10, 11, 12)
    personality_points1 = models.CharField(max_length=50, default='-')
    personality_points2 = models.CharField(max_length=50, default='-')
    personality_points3 = models.CharField(max_length=50, default='-')
    personality_points4 = models.CharField(max_length=50, default='-')
    # Females (9, 10, 11, 12)
    personality_points5 = models.CharField(max_length=50, default='-')
    personality_points6 = models.CharField(max_length=50, default='-')
    personality_points7 = models.CharField(max_length=50, default='-')
    personality_points8 = models.CharField(max_length=50, default='-')
    # Links 
    personality_link    = models.CharField(max_length=200, default='-')

    @property
    def all_questions(self):
        return self.questions.all()

    @property
    def first_three_questions(self):
        return self.questions.all()[0:3]

    @property
    def middle_three_questions(self):
        return self.questions.all()[3:6]

    @property
    def last_three_questions(self):
        return self.questions.all()[6:9]

class Question(models.Model):
    question_type = models.ForeignKey(Personality, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

# Not implemented currently.
#class Result(models.Model):
#    ip_address  = models.CharField(max_length=100)
#    user_agent  = models.CharField(max_length=1000)
#    date        = models.DateTimeField()
