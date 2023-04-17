import requests
import urllib.parse
import json

my_key = "AIzaSyCCUxmWVoEIQJHcJ3Mx5FMAbcC4dzXtBYY"

class Location:
   def __init__(self, name):
      self.name = name

   def distance_to(self, destination):
      url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
      params = {"origins" : self.name, "destinations" : destination, "uints" : "metric", "key" : my_key}
      url = url + urllib.parse.urlencode(params)

      response = requests.get(url)
      response = json.loads(response.text)

      return response['rows'][0]['elements'][0]['distance']['text']


def main():
   origin   = Location(input("From: "))
   distance = origin.distance_to(input("To: "))
   print("Distance: {}".format(distance))

if __name__ == "__main__":
   main()

