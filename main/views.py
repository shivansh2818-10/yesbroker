from django.shortcuts import render
from .models import Property

def PropertiesDataForHomePage():
	data = Property.objects.all()
	print(data)

def HomePage(request):
	return render(request, 'new/homepage.html')

def PropertyFeed(request):
	data = Property.objects.all()
	for propertyIndex in range(len(data)):
		data[propertyIndex].RERA = data[propertyIndex].RERA.lower()
		data[propertyIndex].ratings = data[propertyIndex].Ratings.split("(")[0]
		data[propertyIndex].reviews = data[propertyIndex].Ratings.split("(")[1].rstrip(")")
		data[propertyIndex].land = data[propertyIndex].Society_Configuration_1.split(",")[0].split(":")[1].lstrip()
		data[propertyIndex].blocks = data[propertyIndex].Society_Configuration_1.split(",")[1].split(":")[1].lstrip()
		data[propertyIndex].floors = data[propertyIndex].Society_Configuration_1.split(",")[2].split(":")[1].lstrip()
		data[propertyIndex].units = data[propertyIndex].Society_Configuration_1.split(",")[3].split(":")[1].lstrip()
	return render(request, 'new/propertyfeed.html', {'properties':data})

def PropertyPage(request, propertyId):
	data = Property.objects.get(id=propertyId)
	data.RERA = data.RERA.lower()
	data.ratings = data.Ratings.split("(")[0]
	data.reviews = data.Ratings.split("(")[1].rstrip(")")
	data.land = data.Society_Configuration_1.split(",")[0].split(":")[1].lstrip()
	data.blocks = data.Society_Configuration_1.split(",")[1].split(":")[1].lstrip()
	data.floors = data.Society_Configuration_1.split(",")[2].split(":")[1].lstrip()
	data.units = data.Society_Configuration_1.split(",")[3].split(":")[1].lstrip()
	return render(request, 'PropertyPage.html', {'data':data, 'list':[i for i in range(5)]})