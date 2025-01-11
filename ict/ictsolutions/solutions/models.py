from django.db import models

class Solution(models.Model):    
    slug = models.SlugField()
    solution = models.TextField(max_length=1500)
    clase = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add = True)
    link = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    
def __str__(self):
        return f"{self.solution[:40]}... | Clase: {self.clase} | Date: {self.date.strftime('%Y-%m-%d')} | Link: {self.link} | Likes: {self.likes} | | Dislikes: {self.dislikes}"

def snippet(self):
    return self.body[:100]+'...'

    
   
