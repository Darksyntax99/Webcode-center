from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator 

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

# Review model 
class Review(models.Model):
#Review details 
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey( 
        Course,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    content = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'
    
