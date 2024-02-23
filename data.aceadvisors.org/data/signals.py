from venv import create
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import *
import csv, string, random

'''  
csv template:
    year, data_name
    2000, 50010
    2001, 32110
    2002, 55210
    2003, 12014
'''

def random_string_generator(size=14, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_slug():
    new_string = random_string_generator()
    try:
        AceData.objects.get(slug=new_string)
        create_slug()
    except Exception as e:
        return new_string

@receiver(post_save, sender=AceData)
def print_region(sender, instance, created, **kwargs):
    if created:
        new_slug = create_slug()
        instance.slug = new_slug
        if instance.data!=None:
            with open(instance.data.path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                year = []
                data = []
                for row in csv_reader:
                    try:
                        year.append(int(row[0]))
                        data.append(int(row[1]))
                    except ValueError as e:
                        year.append(row[0])
                        data.append(row[1])

                instance.years_list = str(year[1:])
                instance.data_numbers = str(data[1:])

        if instance.keywords==None:
            instance.keywords = instance.name.lower() + ',' + instance.keywords
            
        instance.save()