import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
from django.utils import timezone

class Asset(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
    ]

    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]

    OS_CHOICES = [
        ('Windows 11 Pro', 'Windows 11 Pro'),
        ('Windows 10 Pro', 'Windows 10 Pro'),
        ('macOS Sonoma', 'macOS Sonoma'),
        ('macOS Ventura', 'macOS Ventura'),
        ('Ubuntu 22.04', 'Ubuntu 22.04'),
        ('Other', 'Other'),
    ]

    RAM_CHOICES = [
        ('8GB', '8GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB'),
        ('64GB', '64GB'),
        ('Other', 'Other'),
    ]

    CPU_CHOICES = [
        ('Intel Core i5', 'Intel Core i5'),
        ('Intel Core i7', 'Intel Core i7'),
        ('Intel Core i9', 'Intel Core i9'),
        ('Apple M1', 'Apple M1'),
        ('Apple M2', 'Apple M2'),
        ('Apple M3', 'Apple M3'),
        ('AMD Ryzen 5', 'AMD Ryzen 5'),
        ('AMD Ryzen 7', 'AMD Ryzen 7'),
        ('Other', 'Other'),
    ]

    EXTERNAL_STORAGE_CHOICES = [
        ('None', 'None'),
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
        ('M.2 NVMe', 'M.2 NVMe'),
        ('External Hub', 'External Hub'),
        ('Docking Station', 'Docking Station'),
        ('Other', 'Other'),
    ]

    STORAGE_SIZE_CHOICES = [
        ('N/A', 'N/A'),
        ('256GB', '256GB'),
        ('512GB', '512GB'),
        ('1TB', '1TB'),
        ('2TB', '2TB'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    asset_model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    ram = models.CharField(max_length=50, choices=RAM_CHOICES, default='16GB')
    os = models.CharField(max_length=50, choices=OS_CHOICES, default='Windows 11 Pro')
    cpu = models.CharField(max_length=50, choices=CPU_CHOICES, default='Intel Core i7')
    purchase_date = models.DateField(null=True, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='New')
    external_storage = models.CharField(max_length=100, choices=EXTERNAL_STORAGE_CHOICES, default='None', blank=True, null=True)
    external_storage_size = models.CharField(max_length=50, choices=STORAGE_SIZE_CHOICES, default='N/A', blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.serial_number}"

    def save(self, *args, **kwargs):
        # Generate QR code after saving if it's a new instance to get the ID
        if not self.id:
            super().save(*args, **kwargs)
            
        if not self.qr_code:
            # Using your local IP so your phone can access it on the same Wi-Fi
            qr_image = qrcode.make(f"http://192.168.1.191:3000/asset/{self.id}")
            canvas = BytesIO()
            qr_image.save(canvas, format='PNG')
            file_name = f'qr-{self.serial_number}.png'
            self.qr_code.save(file_name, File(canvas), save=False)
            # Save again to store the qr_code path, but don't force_insert this time
            super().save(update_fields=['qr_code'])
        else:
            super().save(*args, **kwargs)

class Assignment(models.Model):
    SHIFT_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Morning', 'Morning (9 AM - 1 PM)'),
        ('Evening', 'Evening (2 PM - 6 PM)'),
    ]
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='assignments')
    employee_name = models.CharField(max_length=100)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, default='Full-time')
    assignment_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.asset.name} assigned to {self.employee_name}"

class ChatHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='chat_histories')
    user_query = models.TextField()
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support Chat for {self.asset.name} at {self.timestamp}"
