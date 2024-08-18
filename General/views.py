from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .form import form_doctor,CustomLoginForm,form_patient,Doctor_Form_edite,MedicationForm,PrescriptionForm,patient_Form_edite, add_prescription_formset, add_prescription_formset2,set_appointment,Appointment_edit,add_superuser,superuser_Form_edite,PrescriptionForm,AddPrescriptionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Patient,doctor,Medication,Prescription,AddPrescription,Appointment,superuser
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.forms import modelformset_factory





@login_required
def add_doctor(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            formset = form_doctor(request.POST)
            if formset.is_valid():
                # ذخیره فرم و ایجاد پزشک
                doctor = formset.save()
                
                # افزودن کاربر به گروه "Doctor"
                user = doctor.user  # فرض بر این است که پزشک دارای کاربری است که به آن مربوط است
                doctor_group = Group.objects.get(name='Doctor')  # دریافت گروه "Doctor"
                user.groups.add(doctor_group)  # افزودن کاربر به گروه
                
                return HttpResponse('Doctor created and added to group')
        else:
            formset = form_doctor()
        
        return render(request, 'singup_doctor.html', {'form': formset})
    else:
        return HttpResponse("jost personal can add doctor")


def add_patient(request):
    if request.method == 'POST':
        formset = form_patient(request.POST)
        if formset.is_valid():
            # ذخیره فرم و ایجاد پزشک
            patient = formset.save()
            
            # افزودن کاربر به گروه "Doctor"
            user = patient.user  # فرض بر این است که پزشک دارای کاربری است که به آن مربوط است
            patient_group = Group.objects.get(name='Patient')  # دریافت گروه "Doctor"
            user.groups.add(patient_group)  # افزودن کاربر به گروه
            
            return HttpResponse('Patient created and added to group')
    else:
        formset = form_patient()
    
    return render(request, 'singup_patient.html', {'form': formset})



def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
            
                login(request, user)
                return redirect('post_login')
                        
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def post_login_view(request):
    if request.user.is_superuser:
        try:
            message = superuser.objects.get(user=request.user)
            return render(request, 'welcome1.html', {'message': message})
        except:
            return render(request, 'welcome.html')

    
    elif request.user.groups.filter(name='Doctor').exists():
        message = doctor.objects.get(user=request.user)
        return render(request, 'welcome2.html', {'message': message})
    
    else:
        message = Patient.objects.get(user=request.user)
        return render(request, 'welcome3.html', {'message': message})
    
    


def logout(request):
    auth_logout(request)  # خروج کاربر
    return redirect('login')

@login_required
def show_notactivat (request):
    if request.user.is_superuser:
        test = User.objects.filter(is_active= 'False')
        return render(request, 'show_notactivat.html', {'test': test})
    else:
        return HttpResponse('just personal can acctiv')


def user_activ (request , user_id):

    if request.user.is_superuser:

        user = get_object_or_404(User, id=user_id)
        
        user.is_active = True
        user.save()
        return HttpResponse(f'User {user.username} has been activated.')
    else:
        return HttpResponse('just personal can acctiv')


def find_way (request):

    if request.user.is_authenticated:
        return redirect('post_login')
    else :
        return render(request, 'singup_login.html')

class DoctorUpdateView(UpdateView):
    
    model = doctor
    form_class = Doctor_Form_edite
    template_name = 'edit_doctor.html'
    success_url = reverse_lazy('post_login')

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        """
        obj = get_object_or_404(doctor,user=self.request.user)
        return obj
    

class PatiemtUpdateView(UpdateView):
    model = Patient
    form_class = patient_Form_edite
    template_name = 'edit_patient.html'
    success_url = reverse_lazy('post_login')

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        """
        obj = get_object_or_404(Patient,user=self.request.user)
        return obj
        
class superuserUpdateView(UpdateView):
    model = superuser
    form_class = superuser_Form_edite
    template_name = 'edit_superuser.html'
    success_url = reverse_lazy('post_login')

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        """
        obj = get_object_or_404(superuser,user=self.request.user)
        return obj
    
@login_required
def show_patient_list(request):
    if request.user.is_superuser or request.user.groups.filter(name='Doctor').exists():
        show = Patient.objects.all()
        return render(request, 'show_patient_list.html', {'show': show})
    else:
        return HttpResponse('just personal can show patient list')

@login_required
def show_patient_ditail(request,id):
    if request.user.is_superuser or request.user.groups.filter(name='Doctor').exists():
        show = Patient.objects.get(id = id)
        return render(request, 'show_patient_ditail.html', {'show': show})
    else:
        return HttpResponse('just personal can show patient ditail')

@login_required
def show_doctor_list(request):
    if request.user.is_superuser:        
        show = doctor.objects.all()
        return render(request, 'show_doctor_list.html', {'show': show})
    else:
        return HttpResponse('just personal can show doctor list')    

@login_required
def show_doctor_ditail(request,id):
    if request.user.is_superuser:        
        show = doctor.objects.get(id = id)
        return render(request, 'show_doctor_ditail.html', {'show': show})
    else:
        return HttpResponse('just personal can show doctor list')       

class MedicationCreateView(CreateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'medication_form.html'
    success_url = reverse_lazy('post_login')



@login_required
def medication_category_list(request):
    # دریافت تمامی داروها
    pill = Medication.objects.filter(Medication_type = 'pill')
    Sherbet = Medication.objects.filter(Medication_type = 'Sherbet')
    serum = Medication.objects.filter(Medication_type = 'serum')
    ampoule = Medication.objects.filter(Medication_type = 'ampoule')
    powder = Medication.objects.filter(Medication_type = 'powder')

    # دریافت دسته‌بندی‌های یکتا
    categories = Medication.objects.values_list('Medication_type', flat=True).distinct()
    
    return render(request, 'medication_category_list.html', {'pill': pill,'Sherbet': Sherbet,'serum': serum,'ampoule': ampoule,'powder': powder,'categories': categories})


@login_required
def medication_detail(request, pk):

    medication = get_object_or_404(Medication, pk=pk)
    
    return render(request, 'medication_detail.html', {'medication': medication})




@login_required
def show_add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        formset = add_prescription_formset(request.POST, prescription=form.instance.pk if form.is_valid() else None)
        if form.is_valid() and formset.is_valid():
            prescription = form.save()  # ذخیره نسخه
            for form in formset:
                add_prescription = form.save(commit=False)
                add_prescription.prescription = prescription
                add_prescription.save()
            return redirect('post_login')  # هدایت بعد از موفقیت
    else:
        form = PrescriptionForm()
        formset = add_prescription_formset()

    return render(request, 'show_add_prescription.html', {'form': form, 'formset': formset})


@login_required
def show_prescription_list(request):
    
    if request.user.is_superuser or request.user.groups.filter(name='Doctor').exists():

        show = Prescription.objects.all()
        return render(request, 'show_prescription_list2.html', {'show': show})
    
    else :    
        show = Prescription.objects.filter(patient = request.user.patient)
        return render(request, 'show_prescription_list.html', {'show': show})
    
@login_required
def show_prescription_detail(request,id):
    
    show = AddPrescription.objects.filter(prescription = id)
    show2 = Prescription.objects.get(id = id)

    return render(request, 'show_prescription_detail.html', {'show': show , 'show2': show2 })


@login_required
def set_Appointment(request):

    if request.method == 'POST':
        form = set_appointment(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponse('set Appointment')
    else:
        form = set_appointment()
    
    return render(request, 'set_Appointment.html', {'form': form})

@login_required
def Appointment_list(request):

    if request.user.is_superuser:
        
        show = Appointment.objects.filter(end = False)
        return render(request, 'Appointment_list.html', {'show': show})

    elif request.user.groups.filter(name='Doctor').exists():

        show = Appointment.objects.filter(Doctor = request.user.doctor,end = False)
        return render(request, 'Appointment_list.html', {'show': show})
    
    elif request.user.groups.filter(name='Patient').exists():

        show = Appointment.objects.filter(patient = request.user.patient,end = False)
        return render(request, 'Appointment_list.html', {'show': show})
    
class Appointment_edite(UpdateView):
    model = Appointment
    form_class = Appointment_edit
    template_name = 'Appointment_edit.html'
    success_url = reverse_lazy('Appointment_list')

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        """
        obj = get_object_or_404(Appointment,id=self.kwargs['id'])
        return obj
    
@login_required
def deactive_avtive_Appointment(request,id):
    appointment = Appointment.objects.get(id = id)

    if appointment.status:
        appointment.status = False
        appointment.save()
        return redirect('Appointment_list')

    else :
        appointment.status = True
        appointment.save()
        return redirect('Appointment_list')
    
@login_required
def end_Appointment(request,id):
    
    appointment = Appointment.objects.get(id = id)

    appointment.end = True
    appointment.save()
    return redirect('Appointment_list')




@login_required
def Appointment_end_list(request):

    if request.user.is_superuser:
        
        show = Appointment.objects.filter(end = True)
        return render(request, 'Appointment_end_list.html', {'show': show})

    elif request.user.groups.filter(name='Doctor').exists():

        show = Appointment.objects.filter(Doctor = request.user.doctor,end = True)
        return render(request, 'Appointment_end_list.html', {'show': show})
    
    elif request.user.groups.filter(name='Patient').exists():

        show = Appointment.objects.filter(patient = request.user.patient,end = True)
        return render(request, 'Appointment_end_list.html', {'show': show})
    

@login_required
def add_superusers(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            formset = add_superuser(request.POST)
            if formset.is_valid():
                # ذخیره فرم و ایجاد پزشک
                superuser = formset.save()
                
                
        else:
            formset = add_superuser()
        
        return render(request, 'singup_superuser.html', {'form': formset})
    else:
        return HttpResponse("jost personal can add personal")
    



from django.forms import modelformset_factory

def edit_prescription(request, id):
    prescription = get_object_or_404(Prescription, pk=id)
    AddPrescriptionFormSet = modelformset_factory(AddPrescription, form=AddPrescriptionForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        formset = AddPrescriptionFormSet(request.POST, queryset=AddPrescription.objects.filter(prescription=prescription))

        if form.is_valid() and formset.is_valid():
            prescription = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.prescription = prescription
                instance.save()
            formset.save_m2m()
            return redirect('post_login')
    else:
        form = PrescriptionForm(instance=prescription)
        formset = AddPrescriptionFormSet(queryset=AddPrescription.objects.filter(prescription=prescription))

    return render(request, 'edit_prescription.html', {'form': form, 'formset': formset, 'prescription': prescription})
