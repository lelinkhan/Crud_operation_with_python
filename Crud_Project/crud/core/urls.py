from django.urls import path
from .views import Home,Add_student,Delete_student,Edit_student

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-student/', Add_student.as_view(), name='add_student'),
    path('delete-student/', Delete_student.as_view(), name='delete_student'),
    path('edit-student/<int:id>/', Edit_student.as_view(), name='edit_student')
]