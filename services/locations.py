# services/locations.py

import requests


class LocationService:

    def __init__(self):
        self.api_key = "YOUR_OPENCAGE_API_KEY"
        self.base_url = "https://api.opencagedata.com/geocode/v1/json"

    def get_location_from_coordinates(self, latitude, longitude):

        try:

            params = {
                "q": f"{latitude},{longitude}",
                "key": self.api_key
            }

            response = requests.get(self.base_url, params=params, timeout=10)

            if response.status_code != 200:
                return {"error": "Failed to fetch location"}

            data = response.json()

            if not data["results"]:
                return {"error": "No location data found"}

            components = data["results"][0]["components"]

            location_data = {
                "city": components.get("city")
                or components.get("town")
                or components.get("village"),

                "state": components.get("state"),
                "country": components.get("country"),

                "latitude": latitude,
                "longitude": longitude
            }

            return location_data

        except Exception as e:

            return {
                "error": str(e)
            }