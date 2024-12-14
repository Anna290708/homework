from django.db import models

class CategoryManager(models.Manager):
    def with_item_count(self):
        return self.annotate(item_count=models.Count('items'))
    
class ItemManager(models.Manager):
    def with_tag_count(self):
        return self.annotate(tags_count=models.Count('tags'))
    
class TagManager(models.Manager):
    def popular_tags(self,min_items):
        item=self.annotate(item_count=models.Count('items'))
        return item.filter(item_count__gte=min_items)


    

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categories=CategoryManager()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    items=ItemManager()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tags', blank=True)
    tags=TagManager()

    def __str__(self):
        return self.name
