from django.core.management.base import BaseCommand
from shop.models import Tag, Item, Category
from typing import Any


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        # catgories = Category.objects.with_item_count()
        # for catgeory in catgories:
        #     print(f"category:{catgeory.name}, items count: {catgeory.items_count}")
        
        # items = Item.objects.with_tag_count()
        # for item in items:
        #     print(f"item{item.name}, tags count: {item.tags_count}")

        popular = Tag.objects.popular_tags(3)
        for tag in popular:
            print(f"Tag:{tag.name}, items count: {tag.items_count}")