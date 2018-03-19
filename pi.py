import math
# import argparse

# So box is gonna be 100x100 and radius of circle is going to be diameter/2 is 50
# parser = argparse.ArgumentParser()
# parser.add_argument('--weight', default=1000, help="this number pow2 is the number of dots to check. Higher makes things slower but more precise", type=int)
# args = parser.parse_args()
diameter = 10000

print("Calculate PI by precision of " + str(diameter*diameter)+  " tries")

dots_in_circle = 0
dots_total = 0
center = diameter/2
radius = diameter/2

for i in range(0,diameter):
    for j in range(0,diameter):
        dots_total += 1
        # I am working on X, Y, use pythagoras to calculate the distance from center.
        x_distance_from_center = center-i
        if (x_distance_from_center < 0):
            # make the number positive
            x_distance_from_center *= -1
        y_distance_from_center = center-j
        if (y_distance_from_center <0 ):
            y_distance_from_center *= -1
        
        distance_from_center = math.sqrt(x_distance_from_center*x_distance_from_center + y_distance_from_center * y_distance_from_center)
        if (distance_from_center <= radius):
            dots_in_circle +=1 
        

print(dots_in_circle, dots_total)
print(4*(float(dots_in_circle)/float(dots_total)))
