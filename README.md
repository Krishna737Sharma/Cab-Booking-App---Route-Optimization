# Cab Booking App - Route Optimization

This project involves optimizing the route selection for a cab booking app in a city with 50 key locations. The goal is to implement the All Pair Shortest Path (APSP) algorithm to calculate the shortest paths between all pairs of locations in the city. The city is represented as a graph where nodes correspond to locations, and edges represent the roads connecting them, with weights corresponding to the distance between locations.

## Problem Description

Given a graph representing the city with 50 nodes (locations) and weighted edges (distances between locations), your task is to calculate the shortest path between any two locations using the All Pair Shortest Path (APSP) algorithm.

### Input

- **Distance Matrix**: A symmetric 50x50 distance matrix where:
  - `distance[i][j]` represents the distance (in kilometers) between location `i` and location `j`.
  - The matrix is symmetric, meaning `distance[i][j] == distance[j][i]`.
  - The diagonal elements (`distance[i][i]`) are `0`, as the distance from any location to itself is zero.
  
- **Location Names**: A list of 50 named locations corresponding to the rows and columns of the distance matrix. These locations represent a mix of common urban areas, landmarks, and points of interest (POI) typically found in a city.

### List of 50 Named Locations

1. Airport
2. Central Station
3. City Hall
4. University
5. Downtown Mall
6. Business Park
7. Tech Hub
8. Old Town Square
9. Residential Zone 1
10. Residential Zone 2
11. Residential Zone 3
12. Residential Zone 4
13. Main Library
14. Museum of Art
15. Convention Center
16. Sports Arena
17. City Park
18. Waterfront
19. Harbor
20. Industrial District
21. Zoo
22. Hospital
23. Police Station
24. Fire Station
25. Train Depot
26. Shopping Plaza
27. Cinema Complex
28. Amusement Park
29. Botanical Gardens
30. Golf Course
31. City Market
32. Cathedral
33. Historical Museum
34. Luxury Hotel
35. Suburban Area 1
36. Suburban Area 2
37. Tech Campus
38. Warehouse District
39. Tech Research Center
40. Local Stadium
41. Art Gallery
42. Public Swimming Pool
43. Concert Hall
44. Fitness Center
45. Urban Plaza
46. Food Court
47. Science Museum
48. Bridgeview
49. City Outskirts
50. Recreation Center

### Output

The program will output the shortest paths between all pairs of locations. The result should display the shortest distance and the path taken for each pair of locations. Additionally, the program should allow querying the shortest path between any two given locations.

## Approach

### Algorithm

The All Pair Shortest Path (APSP) algorithm will be implemented using **Floyd-Warshall** or **Johnson's algorithm**, depending on the complexity requirements. This algorithm will calculate the shortest path between all pairs of locations in the graph.

1. **Initialization**: The distance matrix will be used to initialize the graph.
2. **Algorithm Execution**:
   - **Floyd-Warshall Algorithm**: This dynamic programming algorithm computes the shortest paths between all pairs of nodes.
   - **Alternative**: If needed, **Johnson's algorithm** can be used for sparse graphs.
3. **Output**: The shortest distance between each pair of locations and the specific path taken.

### Time Complexity

- **Floyd-Warshall**: The time complexity is O(n³), where `n` is the number of nodes (locations) in the graph. This is feasible for a graph with 50 nodes.
- **Johnson's Algorithm**: The time complexity is O(n² log n + n³), depending on the graph's density.

## How to Run the Code

### Prerequisites

- Python 3.x
- Install necessary libraries:
  ```bash
  pip install numpy networkx
