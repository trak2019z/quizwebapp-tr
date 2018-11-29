from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    """ Model pomocniczy dla użytwkonika. Ma on na celu odróżnienie studenta od nauczyciela."""
    is_student = models.BooleanField(default=False, help_text="Zmienna oznaczająca bycie studentem")
    is_teacher = models.BooleanField(default=False, help_text="Zmienna oznaczająca bycie nauczycielem")


class Subject(models.Model):
    """ Model dla przedmiotu, zawiera on nazwę,kolor oraz funkcje get_html_badge()."""
    name = models.CharField(max_length=30, help_text="Nazwa przedmiotu")
    color = models.CharField(max_length=7, default='#007bff', help_text="Kolor dla tagu")

    def __str__(self):
        return self.name

    def get_html_badge(self):
        """ Funkcja która wyświetla nazwę oraz kolor tagu w kodzie HTML"""
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    """ Model Quiz zawiera klucz obcy twórcy (nauczyciela), nazwę quizzu oraz klucz obcy przedmiotu z jakiego jest quiz."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes', help_text="Twórca")
    name = models.CharField(max_length=255, help_text="Nazwa quizu")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes', help_text="Przedmiot")

    def __str__(self):
        return self.name


class Question(models.Model):
    """ Model Pytanie posiada klucz obcy do quizu oraz treść pytania."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', help_text="Klucz obcy quizu")
    text = models.CharField('Question', max_length=255, help_text="Treść pytania")

    def __str__(self):
        return self.text


class Answer(models.Model):
    """ Model Odpowiedzi posiada klucz obcy do pytania, tekst odpowiedzi oraz pole flagi czy dana odpowiedź jest prawidłowa."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers',
                                 help_text="Klucz obcy pytania")
    text = models.CharField('Answer', max_length=255, help_text="Odpowiedź")
    is_correct = models.BooleanField('Correct answer', default=False,
                                     help_text="Flaga czy dana odpowiedź jest poprawna")

    def __str__(self):
        return self.text


class Student(models.Model):
    """ Model Student posiada pole jeden do jednego z Używkownikiem, oraz powiązania do Modeli Quiz i Subject.
    Posiada też funkcja get_unanswered_questions(quiz)."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, help_text="Użytkownik")
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz', help_text="Quizy")
    interests = models.ManyToManyField(Subject, related_name='interested_students', help_text="Przedmioty")

    def get_unanswered_questions(self, quiz):
        """ Funkcja ta sprawdza czy student dla danego quizu ma jakeiś odpowiedzni nie zaznaczone"""
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    """ Model TakenQuiz posiada klucz obcy dla studenta, klucz obcy do quizu, wynik i date wykonania quizu"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes',
                                help_text="Klucz obcy studenta")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes', help_text="Klucz obcy quizu")
    score = models.FloatField(help_text="Wynik quizu")
    date = models.DateTimeField(auto_now_add=True, help_text="Data wykonania quizu")


class StudentAnswer(models.Model):
    """ Model StudentAnswer posiada klucz obcy studenta oraz klucz obcy odpowiedzi"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers',
                                help_text="Klucz obcy studenta")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+', help_text="Klucz obcy odpowiedzi")
