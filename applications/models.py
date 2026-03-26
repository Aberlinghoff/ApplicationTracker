from django.db import models

# Create your models here.

class JobApplication(models.Model):

    class Status(models.TextChoices):

        SUBMITTED = "su", "Submitted"

        DECLINED_BY_COMPANY = "dbc", "Declined by company"

        USER_DECLINED_OFFER = "udc", "User declined offer"

        OFFER_RECEIVED = "or", "Offer received"

        ACCEPTED_OFFER = "ao", "Accepted offer"

    status = models.CharField(max_length=50, choices=Status.choices, default=Status.SUBMITTED)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    date_applied = models.DateField()
    notes = models.TextField(blank=True, null=True)
