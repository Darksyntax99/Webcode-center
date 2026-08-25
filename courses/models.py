from django.db import models

# Course model.
class Course(models.Model):
    # Course details 
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


# Lessons model 
class Lesson(models.Model):
   # Lessons details
   course = models.ForeignKey(
       Course,
       on_delete=models.CASCADE,
       related_name='lessons'
   )
   title = models.CharField(max_length=100)
   content = models.TextField()
   order = models.PositiveIntegerField(default=1)

   def __str__(self):
       return self.title
