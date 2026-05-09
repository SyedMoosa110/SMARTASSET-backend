import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from inventory.models import Asset

def populate_assets():
    models = ['MacBook Pro', 'Dell XPS 15', 'ThinkPad X1 Carbon', 'HP Spectre x360', 'Surface Laptop 5']
    cpus = ['Intel i7', 'Intel i9', 'Apple M2 Pro', 'AMD Ryzen 9', 'Intel i5']
    rams = ['16GB', '32GB', '64GB', '8GB']
    oss = ['macOS Ventura', 'Windows 11', 'Ubuntu 22.04', 'macOS Sonoma']

    for i in range(1, 21):
        Asset.objects.create(
            name=f"Laptop {i:03d}",
            asset_model=random.choice(models),
            serial_number=f"SN-{random.randint(100000, 999999)}",
            ram=random.choice(rams),
            os=random.choice(oss),
            cpu=random.choice(cpus),
            status='Available'
        )
    print("Successfully created 20 test assets.")

if __name__ == "__main__":
    populate_assets()
