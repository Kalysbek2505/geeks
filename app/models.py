from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Categories', max_length=40)
    


    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(verbose_name='Tags', max_length=40)


    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')


    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
