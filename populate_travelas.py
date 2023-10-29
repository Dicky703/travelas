import os
 
def populate():
	vehicles_cat = add_cat("Ford")

	add_page(cat = vehicles_cat,
		title = "2024-Ford Ranger",
		url = "https://www.ford.com/trucks/ranger/")

	add_page(cat = vehicles_cat,
		title = "Ford-Mustang",
		url = "https://www.ford.com/cars/mustang/")

	add_page(cat = vehicles_cat,
		title = "Ford-Explorer 2024",
		url = "https://www.ford.com/suvs/explorer/")

	add_page(cat = vehicles_cat,
		title = "Ford-Escape",
		url = "https://www.ford.com/suvs-crossovers/escape/")

	vehicles_cat = add_cat("Mercedes")

	add_page(cat = vehicles_cat,
		title = "G-Wagon",
		url = "https://www.mbusa.com/en/vehicles/class/g-class/suv")

	add_page(cat = vehicles_cat,
		title = "S-Class",
		url = "https://www.mbusa.com/en/vehicles/class/s-class/sedan")

	add_page(cat = vehicles_cat,
		title = "C200-Wagon",
		url = "https://www.motortrend.com/reviews/2022-mercedes-benz-c200-wagon-first-drive-review/")

	add_page(cat = vehicles_cat,
		title = "Mercedes-Maybach",
		url = "https://www.mercedes-benz.co.in/?group=all&subgroup=see-all&view=BODYTYPE")

	vehicles_cat = add_cat("Range-Rover")

	add_page(cat = vehicles_cat,
		title = "Discovery",
		url = "https://www.landroverusa.com/discovery/discovery-sport/index.html")

	add_page(cat = vehicles_cat,
		title = "Range-Rover",
		url = "https://www.landroverusa.com/range-rover/range-rover/index.html")

	add_page(cat = vehicles_cat,
		title = "Range-Rover-Velar",
		url = "https://www.landroverusa.com/range-rover/range-rover-velar/index.html")

	add_page(cat = vehicles_cat,
		title = "Range-Rover-Evoque",
		url = "https://www.landroverusa.com/range-rover/range-rover-evoque/index.html")

	vehicles_cat = add_cat("Land-Rover")

	add_page(cat = vehicles_cat,
		title = "Defender-130",
		url = "https://www.landroverusa.com/defender/defender-130/index.html")

	add_page(cat = vehicles_cat,
		title = "Defender-130",
		url = "https://www.landroverusa.com/defender/defender-130/index.html")

	add_page(cat = vehicles_cat,
		title = "Defender-110",
		url = "https://www.landroverusa.com/defender/defender-110/index.html")

	add_page(cat = vehicles_cat,
		title = "Defender-90",
		url = "https://www.landroverusa.com/defender/defender-90/index.html")

	# Printing what we have added to the user.

	for  c  in Car.objects.all():
		for p in Page.objects.filter(car = c):
			print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views = 0):
	p = Page.objects.get_or_create(car = cat, title = title, url = url, views = views)[0]
	return p

def add_cat(name):
	c = Car.objects.get_or_create(name = name)[0]
	return c				
		
# Start excution here

if __name__ == '__main__':
 	print("Starting travelas population script...")
 	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eazzytravel.settings')
 	import django

 	django.setup()
 	from travelas.models import	Car, Page
 	populate()	