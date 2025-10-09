#!/usr/bin/env python3
"""
You are developing a text-based adventure game where players navigate through a series of interconnected rooms. Each room is represented by a node in a graph, and the connections between rooms are represented by edges. Your task is to implement a function that finds the shortest path between two rooms. Given a list of room connections and two room names (start and end), return the shortest path as a list of room names. If no path exists, return an empty list. The room connections are provided as a list of strings, where each string represents a bidirectional connection between two rooms in the format RoomA-RoomB. Room names are unique and case-sensitive.

Example 1:
    Input: ['Kitchen-LivingRoom', 'Bedroom-Bathroom', 'LivingRoom-Bedroom']
    start_room = 'Kitchen'
    end_room = 'Bathroom'
    Output: ['Kitchen', 'LivingRoom', 'Bedroom', 'Bathroom']
    Explanation: The shortest path from Kitchen to Bathroom passes through LivingRoom and Bedroom.

Example 2:
    Input: ['Study-Library', 'Kitchen-DiningRoom', 'Garden-Garage']
    start_room = 'Study'
    end_room = 'Garden'
    Output: []
    Explanation: There is no path connecting Study to Garden, so an empty list is returned.

Requirements:
    1. Implement a function that takes the list of room connections, start room, and end room as input.
    2. Use an appropriate data structure to represent the room graph.
    3. Implement a breadth-first search (BFS) algorithm to find the shortest path.
    4. Return the shortest path as a list of room names, including start and end rooms.
    5. Handle cases where no path exists between the start and end rooms.
    6. Ensure the solution works efficiently for large numbers of rooms and connections.
"""


from collections import deque, defaultdict

def find_shortest_path(room_connections, start_room, end_room):
    # Step 1: Parse connections into a graph
    graph = defaultdict(list)
    for connection in room_connections:
        room_a, room_b = connection.split('-')
        graph[room_a].append(room_b)
        graph[room_b].append(room_a)
    
    # Step 2: Perform BFS
    queue = deque([(start_room, [start_room])])
    visited = set()
    
    while queue:
        current_room, path = queue.popleft()
        
        if current_room == end_room:
            return path  # Shortest path found
        
        if current_room not in visited:
            visited.add(current_room)
            for neighbor in graph[current_room]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    # Step 3: If no path exists
    return []

# Example usage:
connections = ['Kitchen-LivingRoom', 'Bedroom-Bathroom', 'LivingRoom-Bedroom']
start = 'Kitchen'
end = 'Bathroom'
print(find_shortest_path(connections, start, end))  # Output: ['Kitchen', 'LivingRoom', 'Bedroom', 'Bathroom']

connections2 = ['Study-Library', 'Kitchen-DiningRoom', 'Garden-Garage']
start2 = 'Study'
end2 = 'Garden'
print(find_shortest_path(connections2, start2, end2))  # Output: []

