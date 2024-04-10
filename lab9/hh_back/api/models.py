from django.db import models

class Company(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    city = models.CharField(max_length = 50)
    address = models.TextField()

    # def to_json(self):
    #     return {
    #         'id' ; self.id,
    #         'name' : self.name,
    #         'description' : self.description,

    #     }

class Vacancy(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    dalary = models.FloatField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

