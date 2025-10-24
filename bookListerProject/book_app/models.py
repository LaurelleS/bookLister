from django.db import models
import datetime

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    # class similar to an enum to list all genre options (will be a dropdown menu in GUI)
    class Genres(models.TextChoices):
        FANTASY = 'Fantasy'
        SCIENCE_FICTION = 'Science Fiction'
        DYSTOPIAN = 'Dystopian'
        ADVENTURE = 'Adventure'
        ROMANCE = 'Romance'
        MYSTERY = 'Mystery'
        HORROR = 'Horror'
        THRILLER = 'Thriller'
        LGBTQ = 'LGBTQ'
        HISTORICAL_FICTION = 'Historical Fiction'
        YOUNG_ADULT = 'Young Adult'
        CHILD_FICTION = "Children's Fiction"
        AUTOBIOGRAPHY = 'Autobiography'
        BIOGRAPHY = 'Biography'
        SELF_HELP = 'Self-Help'
        HISTORY = 'History'
        HOBBIES = 'Hobbies and Crafts'
        TRUE_CRIME = 'True Crime' 

    genre = models.CharField(
        choices=Genres.choices,
        max_length=100
    )
    date_started = models.DateField(
        default=datetime.date.today # set default start date to when entry is created
    )
    date_ended = models.DateField()

    notes = models.TextField()
    rating = models.SmallIntegerField()

    # class for status choices
    class Status(models.TextChoices):
        NOT_STARTED = "Not Started"
        READING = "Reading"
        DID_NOT_FINISH = "Did Not Finish"
        FINISHED = 'Done'

    status = models.CharField(
        choices=Status.choices,
        max_length=50
    )

    #class for media types
    class MediaType(models.TextChoices):
        EBOOK = "E"
        AUDIOBOOK = 'A'
        PHYSICAL_COPY = 'P'

    media_type = models.CharField(
        choices=MediaType.choices,
        max_length=50
    )

    # uploading photos may require install of Pillow (python -m pip install Pillow)
    cover_photo = models.ImageField( upload_to=lambda instance, filename : 'user_{0}/{1}'.format(instance.user.id, filename) )

    def __str__(self):
        return self.title
