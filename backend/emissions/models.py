from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"


class EmissionRecord(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=100)
    original_value = models.FloatField()
    original_unit = models.CharField(max_length=50)
    normalized_value = models.FloatField()
    normalized_unit = models.CharField(max_length=50)
    co2e = models.FloatField()
    suspicious_flag = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def __str__(self):
        return f"{self.source} - {self.category} - {self.status}"
