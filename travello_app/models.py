from django.db import models

# Create your models here.

class Lang(models.Model):
      name = models.CharField(max_length = 200, db_index = True, null = True)
      
      def __str__(self):
            return self.name

class Book(models.Model):
      title = models.CharField(max_length = 200, db_index = True, null = True)
      isbn = models.CharField(max_length = 13, db_index = True, null = True)
      lang = models.ForeignKey('Lang', on_delete = models.SET_NULL, null = True)
      
      def __str__(self):
            return self.title
      
class Instance(models.Model):
      due_back = models.CharField(max_length = 100, null = True, blank = True, db_index = True)
      book = models.ForeignKey('Book', on_delete= models.CASCADE)
      
      def __str__(self):
            return self.due_back

class Artist(models.Model):
      name = models.CharField(max_length = 200, db_index = True, help_text = 'Artist Name')

      def __str__(self):
            return self.name

class Album(models.Model):
      title = models.CharField(max_length = 200, db_index = True, help_text = 'Album name')
      artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null = True)

      def __str__(self):
            return self.title

class Genre(models.Model):
      name = models.CharField(max_length = 200, db_index = True, help_text = 'Genre Name')

      def __str__(self):
            return self.name

class Track(models.Model):
      title = models.CharField(max_length = 200, db_index = True, help_text = 'Track Nme')
      ratings = models.IntegerField(null = True)
      length = models.IntegerField(null = True)
      count = models.IntegerField(null = True)
      album = models.ForeignKey('Album', on_delete=models.CASCADE)
      genre = models.ForeignKey('Genre', on_delete= models.SET_NULL, null = True)
      
      def __str__(self):
            return self.title