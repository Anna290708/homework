from django.core.management.base import BaseCommand
from shop.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        print(Category.categories.with_item_count())
        print(Item.items.with_tag_count())
        print(Tag.tags.popular_tags(3))