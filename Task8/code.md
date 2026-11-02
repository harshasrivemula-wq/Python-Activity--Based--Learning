## 1. Problem Statement

Develop a **Bus Route Performance Analysis System** to analyze passenger capacity, journey time, fuel usage, and fuel efficiency of different bus routes. The program should identify overloaded routes and determine the most fuel-efficient route.

## 2. Algorithm

1. Start.
2. Enter the number of bus routes.
3. Enter route name, passengers, bus capacity, journey time, and fuel used.
4. Calculate fuel efficiency as passengers divided by fuel used.
5. Store the route details.
6. Check whether the passengers exceed the bus capacity.
7. Display the performance details of each route.
8. Compare the efficiency of each route.
9. Identify the most efficient route.
10. Display the most efficient route and its efficiency.
11. Stop.

## 3. Flowchart
```mermaid id="h6t2vr"
flowchart TD
    A[Start] --> B[Enter number of routes]
    B --> C[Enter route details]
    C --> D[Calculate fuel efficiency]
    D --> E[Store route details]
    E --> F{More routes?}
    F -->|Yes| C
    F -->|No| G[Set first route as best]
    G --> H[Analyze route]
    H --> I[Display route details]
    I --> J{Passengers > Capacity?}
    J -->|Yes| K[Display Overloaded]
    J -->|No| L[Display Normal]
    K --> M{Efficiency > Best Efficiency?}
    L --> M
    M -->|Yes| N[Update best route]
    M -->|No| O[Continue]
    N --> P{More routes to analyze?}
    O --> P
    P -->|Yes| H
    P -->|No| Q[Display most efficient route]
    Q --> R[Display efficiency]
    R --> S[End]
```
## 4. Sample Input

```text id="u2c9kp"
Enter number of routes: 2

Route 1
Enter route name: Route A
Enter passengers: 40
Enter bus capacity: 50
Enter journey time: 2
Enter fuel used: 10

Route 2
Enter route name: Route B
Enter passengers: 60
Enter bus capacity: 50
Enter journey time: 2.5
Enter fuel used: 12
```

## 5. Sample Output

```text id="w7n4sd"
--- Bus Route Analysis ---

Route: Route A
Passengers: 40
Journey Time: 2.0
Fuel Used: 10.0
Efficiency: 4.0
Status: Normal

Route: Route B
Passengers: 60
Journey Time: 2.5
Fuel Used: 12.0
Efficiency: 5.0
Status: Overloaded

Most Efficient Route: Route B
Efficiency: 5.0
```
