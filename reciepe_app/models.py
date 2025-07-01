from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

    

class Recipe(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True,related_name='recipe_user')
    
    slug = models.SlugField(blank=True,null=True,unique=True)
    recipe_disc = models.TextField(blank=True,null=True)
    recipe_img = models.ImageField(upload_to='Recipe_pictures/',null=True,blank=True)
    
    recipe_name = models.CharField(max_length=40,unique=True)
    
    recipe_created_at = models.DateTimeField(auto_now=True)
    recipe_view_count = models.IntegerField(default=1)

    class Meta:
        ordering = ['-recipe_created_at']
        verbose_name = 'Recipe'

    def save(self,*args,**kwargs):
        self.slug = slugify(self.recipe_name)
        super().save(*args,**kwargs)
        if self.slug is None:
            self.slug = slugify(self.recipe_name)
            self.save()

    def __str__(self) -> str:
        return self.recipe_name