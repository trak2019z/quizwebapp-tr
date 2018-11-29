from classroom.api.viewset import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subject', SubjectViewset)
router.register('question', QuestionViewset)
router.register('quiz', QuizViewset)
router.register('answer', AnswerViewset)
router.register('student', StudentViewset)
router.register('studentanswer', StudentAnswerViewset)
router.register('user', UserViewset)
router.register('takenquiz', TakenQuizViewset)


