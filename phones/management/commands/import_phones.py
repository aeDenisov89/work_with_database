import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            Phone.objects.create(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=datetime.strptime(
                    phone['release_date'], '%Y-%m-%d'
                ).date(),
                lte_exists=phone['lte_exists'].strip().lower() == 'true',
            )

