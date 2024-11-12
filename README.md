# map_engine

project_directory/
│
├── src/                        Source code
│   ├── __init__.py             Makes 'src' a package
│   ├── algorithms/             Algorithms module
│   │   ├── __init__.py
│   │   ├── astar.py            Single-destination A* implementation
│   │   ├── multi_stop_astar.py   Multi-stop A* implementation
│   │
│   ├── utils/                  Utility code (optional)
│   │   ├── __init__.py
│   │   ├── graph_loader.py     Code for loading and preparing graphs
│   │   ├── visualization.py    Code for visualizing graphs and paths
│   │
│   ├── main.py                 Main application logic
│
├── tests/                      Unit tests
│   ├── __init__.py
│   ├── test_astar.py           Tests for single-destination A*
│   ├── test_astar_multi.py     Tests for multi-stop A*
│
├── data/                       Data storage
│   ├── blacksburg_road_network.graphml
│
├── docs/                       Documentation
│   ├── algorithms/             Algorithm explanations (optional)
│   │   ├── astar.md            Explanation of single-destination A*
│   │   ├── multi_stop_astar.md   Explanation of multi-stop A*
│   │
│   ├── README.md              Project overview
│
├── requirements.txt           Python dependencies
│
└── README.md                   Root README for the project
