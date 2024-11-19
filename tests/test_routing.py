import unittest
from unittest.mock import patch, Mock
import networkx as nx
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.utils.routing import Routing
import osmnx as ox
import json


class TestRouting(unittest.TestCase):
    
    @classmethod
    def setUp(self) -> None:
        self.graph_path = "../data/LA_road_network.graphml"
        self.road_network = ox.load_graphml(self.graph_path)
        self.router = Routing(self.graph_path)

    
    @patch('requests.get')
    def test_get_coordinates(self,mock_get):
        # All that this function does is do a HTTP GET 
        #Take a base url and pass certain things to it 
        # But only takes the location as string 
        
        #What we need to check is 
        # Is the HTTP response going through ?
        # Is the data fine , does it match
        mock_response = Mock()
        exp_lat,exp_lon = '33.99518','-118.46849'
        
        response_dict = {"lat": "33.99518" , "lon":"-118.46849"}
        
        mock_response.json.return_value = [response_dict]
        
        mock_get.return_value.status_code = 200
        
        mock_get.return_value = mock_response
        
        lat,lon = self.router.get_coordinates('Venice Beach')
        self.assertEqual(lat,33.99518)
        self.assertEqual(lon,-118.46849)
        
        mock_get.assert_called_once_with(
            url="https://nominatim.openstreetmap.org/search",
            params={'q': "Venice Beach", 'format': 'json'},
            headers={'User-Agent': 'Map_Engine/1.0 (sathya05@vt.edu)'}
        )
        
    def test_get_route():
        pass
    
if __name__ == '__main__':
    unittest.main()