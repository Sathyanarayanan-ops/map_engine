# src/main.py
from utils.routing import Routing

def main():
    # Load graph and create Routing instance
    graph_path = "../data/LA_road_network.graphml"
    router = Routing(graph_path)

    # Define locations
    locations = ["Venice Beach, Los Angeles", "Staples Center, Los Angeles", "Griffith Park, Los Angeles"]

    # Get route
    try:
        route = router.get_route(locations)
        print("Route found:", route)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
