# fuel/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from fuel.models import FuelStop
import requests

class RouteOptimizationView(APIView):
    def get(self, request):
        start_location = request.query_params.get('start')
        end_location = request.query_params.get('finish')

        if not start_location or not end_location:
            return Response(
                {"error": "Start and finish locations are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Step 1: Get the route using a free routing API (e.g., OpenRouteService)
            route_api_url = "https://api.openrouteservice.org/v2/directions/driving-car"
            api_key = "YOUR-API-KEY"  # Replace with your actual API key
            params = {
                "api_key": api_key,
                "start": start_location,
                "end": end_location
            }
            response = requests.get(route_api_url, params=params)
            response_data = response.json()


            if response.status_code != 200:
                return Response(
                    {"error": "Failed to fetch the route from the API."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # Extract the route distance and geometry
            # Extract route distance
            route_distance = response_data['features'][0]['properties']['segments'][0]['distance']  # in meters

            # Extract route geometry
            route_geometry = response_data['features'][0]['geometry']['coordinates']  # List of coordinates


            # Step 2: Divide the route into 500-mile segments
            vehicle_range = 500 * 1609.34  # Convert miles to meters
            segments = int(route_distance // vehicle_range) + 1


            # Step 3: Identify optimal fuel stops
            fuel_stops = []
            total_fuel_cost = 0
            for i in range(segments):
                # Query for fuel stops in the segment (dummy logic here, will refine based on segment location)
                nearby_stops = FuelStop.objects.order_by('price_per_gallon')[:5]
                if nearby_stops:
                    cheapest_stop = nearby_stops.first()
                    fuel_stops.append({
                        "name": cheapest_stop.name,
                        "city": cheapest_stop.city,
                        "state": cheapest_stop.state,
                        "price_per_gallon": cheapest_stop.price_per_gallon,
                    })
                    total_fuel_cost += 50 * cheapest_stop.price_per_gallon  # Assume 50 gallons per refuel

            # import pdb; pdb.set_trace()
            # Step 4: Return the response
            return Response({
                "route_geometry": route_geometry,
                "fuel_stops": fuel_stops,
                "total_fuel_cost": total_fuel_cost
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
