from django import forms
from django.contrib.auth.models import User
from .models import doctor,Patient,Medication,Prescription, AddPrescription,Appointment,superuser
from django.contrib.auth.forms import AuthenticationForm
from django.forms import formset_factory , BaseFormSet,inlineformset_factory


class form_doctor(forms.ModelForm):

    username = forms.CharField(max_length=150, help_text='نام کاربری را وارد کنید.')
    password = forms.CharField(widget=forms.PasswordInput(), help_text='رمز عبور را وارد کنید.')

    class Meta:
        model = doctor
        fields = ['first_name', 'last_name', 'full_name', 'Medical_license_number', 'Expertise', 'phone_number','marital_status','gender']

    def save(self, commit=True):
        # ذخیره کاربر جدید
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)
        
        # ذخیره پزشک
        doctor = super().save(commit=False)
        doctor.user = user
        if commit:
            doctor.save()
        return doctor
    

class form_patient(forms.ModelForm):

    username = forms.CharField(max_length=150, help_text='نام کاربری را وارد کنید.')
    password = forms.CharField(widget=forms.PasswordInput(), help_text='رمز عبور را وارد کنید.')

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'full_name', 'National_code', 'underlying_disease', 'phone_number','marital_status','gender']

    def save(self, commit=True):
        # ذخیره کاربر جدید
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password , is_active=False)
        
        # ذخیره پزشک
        patient = super().save(commit=False)
        patient.user = user
        if commit:
            patient.save()
        return patient
    


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class Doctor_Form_edite(forms.ModelForm):
    class Meta:
        model = doctor
        fields = ['first_name', 'last_name', 'full_name','Medical_license_number', 'Expertise', 'phone_number','marital_status', 'gender'] 

class superuser_Form_edite(forms.ModelForm):
    class Meta:
        model = superuser
        fields = ['first_name', 'last_name', 'full_name','Medical_license_number', 'Expertise', 'phone_number','marital_status', 'gender'] 

class patient_Form_edite(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'full_name', 'National_code', 'underlying_disease', 'phone_number','marital_status','gender'] 

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'description', 'Complications','How_to_use', 'expiration_date', 'Production_date','number','Medication_type'] 



class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'type_of_disease']

class AddPrescriptionForm(forms.ModelForm):
    class Meta:
        model = AddPrescription
        fields = ['medication', 'description']

class BaseAddPrescriptionFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        self.prescription = kwargs.pop('prescription', None)
        super().__init__(*args, **kwargs)

    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        if self.prescription is not None:
            kwargs['initial'] = {'prescription': self.prescription}
        return kwargs

add_prescription_formset = formset_factory(AddPrescriptionForm, formset=BaseAddPrescriptionFormSet, extra=1)
add_prescription_formset2 = inlineformset_factory(Prescription, AddPrescription, form=AddPrescriptionForm, extra=1, can_delete=True)


class set_appointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Doctor', 'patient','time', 'disease','descriptien']

class Appointment_edit(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['time'] 




class add_superuser(forms.ModelForm):

    username = forms.CharField(max_length=150, help_text='نام کاربری را وارد کنید.')
    password = forms.CharField(widget=forms.PasswordInput(), help_text='رمز عبور را وارد کنید.')

    class Meta:
        model = superuser
        fields = ['first_name', 'last_name', 'full_name', 'Medical_license_number', 'Expertise', 'phone_number','marital_status','gender']

    def save(self, commit=True):
        # ذخیره کاربر جدید
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_superuser(username=username, password=password)
        
        # ذخیره پزشک
        superuser = super().save(commit=False)
        superuser.user = user
        if commit:
            superuser.save()
        return superuser