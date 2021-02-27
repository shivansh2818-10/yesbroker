from django.db import models

class FilterType(models.Model):
	Filter_Type_Name = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.Filter_Type_Name

class Filter(models.Model):
	Filter_Type_Name = models.ForeignKey(FilterType, null=True, on_delete=models.SET_NULL)
	Filter_Name = models.CharField(max_length=10, null=True)
	Filter_Id = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.Filter_Name

class Product(models.Model):
	Filters = models.ManyToManyField(Filter)
	Category = models.TextField(blank=True, null=True)
	RERA = models.CharField(max_length=3, blank=True, null=True)
	Society = models.CharField(max_length=20, blank=True, null=True)
	Developer = models.CharField(max_length=50, blank=True, null=True)
	Completion = models.CharField(max_length=5, blank=True, null=True)
	Age = models.CharField(max_length=10, blank=True, null=True)
	Ratings = models.CharField(max_length=10, blank=True, null=True)
	Contact = models.CharField(max_length=10, blank=True, null=True)
	Sub_Locality = models.CharField(max_length=50, blank=True, null=True)
	Locality = models.CharField(max_length=20, blank=True, null=True)
	Google_Pin = models.TextField(blank=True, null=True)
	Society_Configuration_1 = models.CharField(max_length=100, blank=True, null=True)
	Society_Configuration_2 = models.CharField(max_length=100, blank=True, null=True)
	Price = models.CharField(max_length=12, blank=True, null=True)
	Promoters_Members = models.TextField(blank=True, null=True)
	Land_Owner_and_Investor_Details = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.Developer