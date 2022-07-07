from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = "Create random new users"

    def add_arguments(self, parser):
        parser.add_argument("user_id", nargs=1, type=int, choices=range(1, 11),
                            help="enter the number of users in the range from 1 to 10 ")

    def handle(self, *args, **options):
        fake = Faker()
        users = []
        for i in range(options["user_id"][0]):
            users.append(User(
                username=fake.user_name(),
                email=fake.email(),
                password=make_password(fake.word() + fake.word()))
            )
        User.objects.bulk_create(users)

