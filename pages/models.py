from django.db import models

# Create your models here.
class Page(models.Model):
    word = models.CharField(max_length=30, primary_key=True)
    word_text = models.TextField()
     
    def words(self):
        return self.word_text.lower().split()

