'''
Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
of the points in your 3-D space and store them in a list. The final output is a list with each
consisting of a point and its nearest neighbour. [Hint: Use distance between two points
formula]
'''
def distance (x1,y1,z1,x2,y2,z2):
    return (x1-x2)*(x1-x2)+ (y1-y2)*(y1-y2) +(z1-z2)*(z1-z2)

points = list(range(10))
for i in range(10):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    z = int(input("Enter z coordinate: "))
    points[i] = (x,y,z)

nearest_neighbours = []
for i in range(10):
    current_point = points[i]
    min_distance = float('inf')
    nearest_point = None
    
    for j in range(10):
        if(i == j):
            continue
        else:
            other_point = points[j]
            current_distance = distance(current_point[0],current_point[1],current_point[2],other_point[0],other_point[1],other_point[2])
            if(current_distance < min_distance):
                min_distance = current_distance
                nearest_point = other_point
    nearest_neighbours.append((current_point,nearest_point))


    print(nearest_neighbours)

        






print(points)


    



    


    
    



