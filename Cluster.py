# -*- coding: utf-8 -*-


import numpy as np


class Cluster:
    """
    Class to represent a Cluster: set of points and their centroid
    """

    def __init__(self, points):
        if len(points) == 0:
            raise Exception("Cluster cannot have 0 Points")
        else:
            self.points = points
            self.dimension = points[0].dimension

        # Check that all elements of the cluster have the same dimension
        for p in points:
            if p.dimension != self.dimension:
                raise Exception(
                    "Point %s has dimension %d different with %d from the rest "
                    "of points") % (p, len(p), self.dimension)

        # Calculate Centroid
        self.centroid = self.calculate_centroid()
        self.converge = False

    def calculate_centroid(self):
        """
        Method that calculates the centroid of the Cluster, calculating
        the average of each of the coordinates of the points
        :return: Centroid of cluster
        """
        sum_coordinates = np.zeros(self.dimension)
        for p in self.points:
            for i, x in enumerate(p.coordinates):
                sum_coordinates[i] += x

        return (sum_coordinates / len(self.points)).tolist()

    def update_cluster(self, points):
        """
        Calculate the new centroid and check if converge
        :param points: list of new points
        :return: updated cluster
        """
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculate_centroid()
        self.converge = np.array_equal(old_centroid, self.centroid)

    def __repr__(self):
        cluster = 'Centroid: ' + str(self.centroid) + '\nDimension: ' + str(
            self.dimension)
        for p in self.points:
            cluster += '\n' + str(p)

        return cluster + '\n\n'
