# map_engine


```python
project_directory/
├── src/                          # Source code
│   ├── algorithms/               # Core algorithm implementations
│   │   ├── astar.py             # Single-destination A* algorithm
│   │   ├── multi_stop_astar.py  # Multi-stop A* implementation
│   │   └── __init__.py
│   ├── utils/                    # Utility modules
│   │   ├── graph_loader.py      # Graph loading and preparation
│   │   ├── visualization.py      # Graph and path visualization
│   │   └── __init__.py
│   ├── main.py                  # Main application entry point
│   └── __init__.py
│
├── tests/                        # Test suite
│   ├── test_astar.py            # Single-destination A* tests
│   ├── test_astar_multi.py      # Multi-stop A* tests
│   └── __init__.py
│
├── data/                        # Data files
│   └── blacksburg_road_network.graphml
│
├── docs/                        # Documentation
│   ├── algorithms/
│   │   ├── astar.md            # Single-destination A* explanation
│   │   └── multi_stop_astar.md # Multi-stop A* explanation
│   └── README.md               # Project overview
│
└── requirements.txt             # Project dependencies

