from django.shortcuts import render
from .models import Product, Filter, FilterType


def HomePage(request):
	return render(request, 'homepage.html')

def PropertyFeed(request):
	if len(request.GET) == 0:
		data = Product.objects.all()
	else:
		data = list()
		for i in request.GET:
			while '%' in i:
				i = i.replace('%', ' ')
			for j in Product.objects.filter(Filters__Filter_Name=i):
				data.append(j)

	for propertyIndex in range(len(data)):
		try:
			data[propertyIndex].RERA = data[propertyIndex].RERA.lower()
		except:
			data[propertyIndex].RERA = 'unavailable'
		try:
			data[propertyIndex].ratings = data[propertyIndex].Ratings.split("(")[0]
		except:
			data[propertyIndex].ratings = 'unavailable'
		try:
			data[propertyIndex].reviews = data[propertyIndex].Ratings.split("(")[1].rstrip(")")
		except:
			data[propertyIndex].reviews = 'unavailable'
		try:
			data[propertyIndex].land = data[propertyIndex].Society_Configuration_1.split(",")[0].split(":")[1].lstrip()
		except:
			data[propertyIndex].land = 'unavailable'
		try:
			data[propertyIndex].blocks = data[propertyIndex].Society_Configuration_1.split(",")[1].split(":")[1].lstrip()
		except:
			data[propertyIndex].blocks = 'unavailable'
		try:
			data[propertyIndex].floors = data[propertyIndex].Society_Configuration_1.split(",")[2].split(":")[1].lstrip()
		except:
			data[propertyIndex].floors = 'unavailable'
		try:
			data[propertyIndex].units = data[propertyIndex].Society_Configuration_1.split(",")[3].split(":")[1].lstrip()
		except:
			data[propertyIndex].units = 'unavailable'

	filterData = dict()
	for filterType in FilterType.objects.all():
		filterData[filterType.Filter_Type_Name] = Filter.objects.filter(Filter_Type_Name__Filter_Type_Name=filterType.Filter_Type_Name)

	return render(request, 'propertyfeed.html', {'properties':data, 'filterData':filterData})

def PropertyPage(request, propertyId):
	data = Product.objects.get(id=propertyId[0])
	data.RERA = data.RERA.lower()
	data.ratings = data.Ratings.split("(")[0]
	data.reviews = data.Ratings.split("(")[1].rstrip(")")
	data.land = data.Society_Configuration_1.split(",")[0].split(":")[1].lstrip()
	data.blocks = data.Society_Configuration_1.split(",")[1].split(":")[1].lstrip()
	data.floors = data.Society_Configuration_1.split(",")[2].split(":")[1].lstrip()
	data.units = data.Society_Configuration_1.split(",")[3].split(":")[1].lstrip()
	return render(request, 'property.html', {'data':data, 'list':[i for i in range(5)]})
