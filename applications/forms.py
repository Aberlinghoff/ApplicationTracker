from .models import JobApplication
from django import forms

# Form for creating and updating job applications
class JobApplicationForm(forms.ModelForm):
    notes = forms.CharField(required=False)
    date_applied = forms.DateField(input_formats=['%m/%d/%Y'])
    company_name = forms.CharField(max_length=255)
    job_title = forms.CharField(max_length=255)
    class Meta:
        model = JobApplication
        fields = [
            'company_name',
            'job_title',
            'date_applied',
            'status',
            'notes'
        ]
