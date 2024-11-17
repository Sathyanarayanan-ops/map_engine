# src/utils/routing.py
from typing import List, Any
import requests
import osmnx as ox

class Routing:
    def __init__(self, graph_path: str):
        self.road_network = ox.load_graphml(graph_path)

    def get_coordinates(self, location: str):
        BASE_URL = "https://nominatim.openstreetmap.org/search"
        PARAMS = {'q': location, 'format': 'json'}
        HEADERS = {'User-Agent': 'Map_Engine/1.0 (sathya05@vt.edu)'}

        response = requests.get(url=BASE_URL, params=PARAMS, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if not data:
            raise ValueError(f"No coordinates found for location: {location}")

        lat, lon = float(data[0]["lat"]), float(data[0]["lon"])
        return lat, lon

    def get_route(self, places: List[str]):
        coordinates = [self.get_coordinates(place) for place in places]
        nodes = [ox.distance.nearest_nodes(self.road_network, X=lon, Y=lat) for lat, lon in coordinates]
        from algorithms import astar_pathfind_multi_stop
        return astar_pathfind_multi_stop(self.road_network, nodes)
