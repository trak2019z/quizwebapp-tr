from classroom.models import Question, Quiz, Subject, Answer, Student, StudentAnswer, User, TakenQuiz
from .serializers import SubjectSerializer, QuestionSerializer, QuizSerializer, StudentSerializer, AnswerSerializer, \
    StudentAnswerSerializer, UserSerializer, TakenQuizSerializer
from rest_framework import viewsets


class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class AnswerViewset(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentAnswerViewset(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TakenQuizViewset(viewsets.ModelViewSet):
    queryset = TakenQuiz.objects.all()
    serializer_class = TakenQuizSerializer
