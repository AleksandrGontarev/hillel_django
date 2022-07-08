from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    _help = "Delete users by id"

    def add_arguments(self, parser):
        parser.add_argument("user_id", nargs="+", type=int, help="enter user id to delete ")

    def handle(self, *args, **options):

        if User.objects.get(is_superuser=True).id in options["user_id"]:
            superuser_id = User.objects.get(is_superuser=1).id
            raise CommandError(f"superuser with id({superuser_id}) in the list, deletion is not possible")
        delete_user = User.objects.filter(pk__in=options["user_id"]).delete()
        self.stdout.write("Delete %s" % delete_user)
