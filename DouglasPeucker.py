#Douglas Peucker Algorithm: to use fewer points to represent a route 

from __future__ import division
from math import sqrt, pow

#parameter
THRESHOLD = 0.0001  

#return the distance between a point and a line
def point2LineDistance(point_a, point_b, point_c):
    if point_b[0] == point_c[0]:
        return 9999999
    slope = (point_b[1] - point_c[1]) / (point_b[0] - point_c[0])
    intercept = point_b[1] - slope * point_b[0]

    distance = abs(slope * point_a[0] - point_a[1] + intercept) / sqrt(1 + pow(slope, 2))
    return distance


class DouglasPeucker(object):
    def __init__(self):
        self.threshold = THRESHOLD
        self.qualify_list = list();
        self.disqualify_list = list();

#point dilution
    def diluting(self, point_list):
        if len(point_list) < 3:
            self.qualify_list.extend(point_list[::-1])
        else:
            #find the point that is the farthest from the line
            max_distance_index, max_distance = 0, 0
            for index, point in enumerate(point_list):
                if index in [0, len(point_list) - 1]:
                    continue
                distance = point2LineDistance(point, point_list[0], point_list[-1])
                if distance > max_distance:
                    max_distance_index = index
                    max_distance = distance

            # if the maximum distance is smaller than threshold, delete all the points in the middle. Otherwise, cut the line.
            if max_distance < self.threshold:
                self.qualify_list.append(point_list[-1])
                self.qualify_list.append(point_list[0])
            else:
                sequence_a = point_list[:max_distance_index]
                sequence_b = point_list[max_distance_index:]

                for sequence in [sequence_a, sequence_b]:
                    if len(sequence) < 3 and sequence == sequence_b:
                        self.qualify_list.extend(sequence[::-1])
                    else:
                        self.disqualify_list.append(sequence)


    def main(self, point_list):
        self.diluting(point_list)
        while len(self.disqualify_list) > 0:
            self.diluting(self.disqualify_list.pop())




