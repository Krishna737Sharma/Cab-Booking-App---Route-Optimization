# Read the data file of distance matrix from city_data.csv
import csv
import numpy as np
dist_mat=np.loadtxt('city_data.csv',delimiter=',')
dist_mat

#Create a list of location names
loc_name=[
'Airport',
'Central Station',
'City Hall',
'University',
'Downtown Mall',
'Business Park',
'Tech Hub',
'Old Town Square',
'Residential Zone 1',
'Residential Zone 2',
'Residential Zone 3',
'Residential Zone 4',
'Main Library',
'Museum of Art',
'Convention Center',
'Sports Arena',
'City Park',
'Waterfront',
'Harbor',
'Industrial District',
'Zoo',
'Hospital',
'Police Station',
 'Fire Station',
'Train Depot',
'Shopping Plaza',
'Cinema Complex',
'Amusement Park',
'Botanical Gardens',
'Golf Course',
'City Market',
'Cathedral',
'Historical Museum',
'Luxury Hotel',
'Suburban Area 1',
'Suburban Area 2',
'Tech Campus',
'Warehouse District',
'Tech Research Center',
'Local Stadium',
'Art Gallery',
'Public Swimming Pool',
'Concert Hall',
'Fitness Center',
'Urban Plaza',
'Food Court',
'Science Museum',
'Bridgeview',
'City Outskirts',
'Recreation Center'  ]

print(len(loc_name))

short_dist=np.full((len(dist_mat),len(dist_mat)),np.inf)
mid_path=[ [ [] for _ in range(len(dist_mat)) ] for _ in range(len(dist_mat)) ]

# Dijkstra's algorithm time complexity O(n^2 logn)
for i in range(len(dist_mat)):
  short_dist[i][i]=0
  visit=set()
  for _ in range(len(dist_mat)):
    min_dis=np.inf
    min_index=-1
    for j in range(len(dist_mat)):
      if j not in visit and short_dist[i][j]<min_dis:
        min_dis=short_dist[i][j]
        min_index=j
    visit.add(min_index)
    for j in range(len(dist_mat)):
      if (short_dist[i][min_index]+dist_mat[min_index][j])<(short_dist[i][j]):
        short_dist[i][j]=short_dist[i][min_index]+dist_mat[min_index][j]
        mid_path[i][j]=mid_path[i][min_index]+[loc_name[j]]

# Print the shortest path
for i in range(len(dist_mat)):
  for j in range(i):
    print(f"Shortest path from {loc_name[i]} to {loc_name[j]}: {short_dist[i][j]} kilometer")
    print(f"Intermidiate path:{loc_name[i]}->{'->'.join(mid_path[i][j])}")
    print("\n")
