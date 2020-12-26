from .models import Personality, Question
from json import loads

def get_all_book_questions():
    """
    This returns the questions in the way that the book presents them.
    """
    questions = []
    for i in range(0, 6):
        for j in Personality.objects.all()[i].first_three_questions:
            questions.append(j)
    for i in range(0, 6):
        for j in Personality.objects.all()[i].middle_three_questions:
            questions.append(j)
    for i in range(0, 6):
        for j in Personality.objects.all()[i].last_three_questions:
            questions.append(j)

    return questions


def get_result(questions, test_id):
    """
    Returns the result in the {personality:value} format according to the appropriate test_id.
    """
    # Get the questions' actual IDs.
    question_IDs = []
    for q in questions: 
        question_IDs.append(q.strip('q'))

    question_objects = list(Question.objects.filter(id__in=question_IDs))

    result = {}
    if(test_id == 1):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points1)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})
        
    elif(test_id == 2):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points2)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})

    elif(test_id == 3):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points3)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})


    elif(test_id == 4):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points4)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})


    elif(test_id == 5):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points5)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})


    elif(test_id == 6):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points6)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})


    elif(test_id == 7):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points7)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})

    elif(test_id == 8):
        for i in range(0, 6):
            l = loads(Personality.objects.all()[i].personality_points8)
            result.update({ Personality.objects.all()[i] : l[len(list(set(Personality.objects.all()[i].all_questions).intersection(question_objects)))]})

    else:
        # This should not happen
        pass

    # Sort the result by their values:
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

    return sorted_result
