from django.urls import path
from . import views
from .views import DoctorUpdateView,MedicationCreateView,PatiemtUpdateView,Appointment_edite,superuserUpdateView

urlpatterns = [
    path('', views.find_way, name='find_way'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_superuser/', views.add_superusers, name='add_superuser'),
    path('patient', views.add_patient, name='add_patient'),
    path('login/', views.login_view, name='login'),
    path('post_login/', views.post_login_view, name='post_login'),
    path('logout/', views.logout, name='logout'),
    path('show_notactivat/', views.show_notactivat, name='show_notactivat'),
    path('user_activ/<int:user_id>/', views.user_activ, name='user_activ'),
    path('edit_doctor/', DoctorUpdateView.as_view(), name='edit_doctor'),
    path('edit_superuser/', superuserUpdateView.as_view(), name='edit_superuser'),
    path('edit_patient/', PatiemtUpdateView.as_view(), name='edit_patient'),
    path('add_medication/', MedicationCreateView.as_view(), name='add_medication'),
    path('medications/', views.medication_category_list, name='medication_category_list'),
    path('medications/<int:pk>/', views.medication_detail, name='medication_detail'),
    path('add_prescription/', views.show_add_prescription, name='add_prescription'),
    path('edit_prescription/<int:id>/', views.edit_prescription, name='edit_prescription'),
    path('prescription_list/', views.show_prescription_list, name='prescription_list'),
    path('prescription_detail/<int:id>/', views.show_prescription_detail, name='prescription_detail'),
    path('show_patient_list/', views.show_patient_list, name='show_patient_list'),
    path('show_patient_ditail/<int:id>/', views.show_patient_ditail, name='show_patient_ditail'),
    path('show_doctor_list/', views.show_doctor_list, name='show_doctor_list'),
    path('show_doctor_ditail/<int:id>/', views.show_doctor_ditail, name='show_doctor_ditail'),
    path('set_Appointment/', views.set_Appointment, name='set_Appointment'),
    path('Appointment_list/', views.Appointment_list, name='Appointment_list'),
    path('Appointment_edite/<int:id>/', Appointment_edite.as_view(), name='Appointment_edite'),
    path('deactive_avtive_Appointment/<int:id>/',views.deactive_avtive_Appointment, name='deactive_avtive_Appointment'),
    path('end_Appointment/<int:id>/',views.end_Appointment, name='end_Appointment'),
    path('Appointment_end_list/', views.Appointment_end_list, name='Appointment_end_list'),
]