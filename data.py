# Importing required libraries 
from googleplaces import GooglePlaces, types
from pprint import pprint
import geocoder

g = geocoder.ip('me')
print(g.latlng)
my_lat_lng ={'lat': g.latlng[0], 'lng': g.latlng[1]}
  
# Use your own API key for making api request calls 
API_KEY = 'AIzaSyBr8V0XkaNFYkNXcP6eJc76b6YutvizwNw'
  
# Initialising the GooglePlaces constructor 
google_places = GooglePlaces(API_KEY) 

# storing returned data
# my_places_list
my_places_list = []

# my_places_list = [
#      { name: xyz,
#        local_phone: 5645464,
#        international_phone: +85431
#      },
#      { name: pqr,
#        local_phone: 123456,
#        international_phone: +99999
#      }
# ]


# function to return nearest hospitals data 
def generate_DATA():
    query_result = google_places.nearby_search( 
            # lat_lng ={'lat': 46.1667, 'lng': -1.15}, 
            lat_lng = my_lat_lng, 
            radius = 5000, 
            types =[types.TYPE_HOSPITAL]) 
    

    # If any attributions related  
    # with search results print them 
    if query_result.has_attributions: 
        print (query_result.html_attributions) 

    # Iterate over the search results 
    counter = 0
    for place in query_result.places:
        each_place_dict = {}
        if (counter == 10): break
        counter += 1
        place.get_details()

        # creating a place object of single place
        each_place_dict['1name'] = place.name,
        each_place_dict['2local_phone_num'] = place.local_phone_number,
        each_place_dict['3international_phone_num'] = place.international_phone_number,

        # appending single place dict
        my_places_list.append(each_place_dict)

    # printing list data in terminal
    pprint(my_places_list)
    # returning final data
    return my_places_list
