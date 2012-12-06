from django.core.management.base import BaseCommand, CommandError

from tagging.models import Tag
from tagging.utils import TagNameNormalizer


class Command(BaseCommand):

    help = 'Normalizes all tag names using the current normalization settings'

    def handle(self, *args, **options):
        for tag in Tag.objects.all():
            normalized_name = TagNameNormalizer.normalize(tag.name)
            if normalized_name == tag.name:
                self.stdout.write('Skipping: %s\n' % tag.name)
                continue
            try:
                existing_tag = Tag.objects.get(name=normalized_name)
                self.stdout.write('Merging: %s => %s\n' %
                    (tag.name, existing_tag.name)
                )
                tag.merge_into(existing_tag)
                continue
            except Tag.DoesNotExist:
                self.stdout.write('Renaming: %s => %s\n' %
                    (tag.name, normalized_name)
                )
                tag.name = normalized_name
                tag.save()
        self.stdout.write('Done normalizing tags names.\n')