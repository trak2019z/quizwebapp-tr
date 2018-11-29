from rest_framework import serializers
from classroom.models import Question, Quiz, Subject, Answer, Student, StudentAnswer, User, TakenQuiz


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TakenQuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TakenQuiz
        fields = '__all__'
