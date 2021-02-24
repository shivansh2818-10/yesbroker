from django.db import models

class Property(models.Model):
	Category = models.TextField(blank=True)
	RERA = models.CharField(max_length=3, blank=True)
	Society = models.CharField(max_length=20, blank=True)
	Developer = models.CharField(max_length=50, blank=True)
	Completion = models.CharField(max_length=5, blank=True)
	Age = models.CharField(max_length=10, blank=True)
	Ratings = models.CharField(max_length=10, blank=True)
	Contact = models.CharField(max_length=10, blank=True)
	Sub_Locality = models.CharField(max_length=50, blank=True)
	Locality = models.CharField(max_length=20, blank=True)
	Google_Pin = models.TextField(blank=True)
	Society_Configuration_1 = models.CharField(max_length=100, blank=True)
	Society_Configuration_2 = models.CharField(max_length=100, blank=True)
	Price = models.CharField(max_length=12, blank=True)
	Promoters_Members = models.TextField(blank=True)
	Land_Owner_and_Investor_Details = models.TextField(blank=True)