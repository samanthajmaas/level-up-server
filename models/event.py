from django.db import models

class Event(models.Model):
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value