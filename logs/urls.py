from django.urls import include, path

from .views import logs, admins, guests

urlpatterns = [
    path('', logs.home, name='home'),

        path('admin/', include(([
        path('', admins.QuizListView.as_view(), name='quiz_list'),
        path('interests/', admins.AdminInterestsView.as_view(), name='admin_interests'),
        path('taken/', admins.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('log/<int:pk>/', admins.take_quiz, name='take_quiz'),
        ], 'logs'), namespace='admins')),

        path('guest/', include(([
        path('', guests.QuizListView.as_view(), name='quiz_change_list'),
        path('log/add/', guests.QuizCreateView.as_view(), name='quiz_add'),
        path('log/<int:pk>/', guests.QuizUpdateView.as_view(), name='quiz_change'),
        path('log/<int:pk>/delete/', guests.QuizDeleteView.as_view(), name='quiz_delete'),
        path('log/<int:pk>/results/', guests.QuizResultsView.as_view(), name='quiz_results'),
        path('log/<int:pk>/question/add/', guests.question_add, name='question_add'),
        path('log/<int:quiz_pk>/question/<int:question_pk>/', guests.question_change, name='question_change'),
        path('log/<int:quiz_pk>/question/<int:question_pk>/delete/', guests.QuestionDeleteView.as_view(), name='question_delete'),
        ], 'logs'), namespace='guests')),
]
