from django.db import models
from .school import LearningArea


class Strand(models.Model):
    learningArea = models.ForeignKey(LearningArea, on_delete=models.CASCADE,)
    strand = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.strand}"


class Sub_strand(models.Model):
    strand = models.ForeignKey(Strand, on_delete=models.CASCADE)
    subStrand = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subStrand}"
