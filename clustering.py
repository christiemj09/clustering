"""
Cluster items deemed to be equivalent.
"""

import csv
import sys


class UnionFind(object):
    """
    The union-find data structure.
    
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """

    def __init__(self, data_points):
    
        self.sets = {}        
        
        for data_point in data_points:
            self.sets[data_point] = {'name':None, 'size':1}
    
    def union(self, set_nameA, set_nameB):
        """Combine two sets of nodes, making their elements belong to the same set."""
        
        rep_nameA = self.find(set_nameA)
        rep_nameB = self.find(set_nameB)
        
        if rep_nameA == rep_nameB:
            return
    
        if self.sets[rep_nameA]['size'] > self.sets[rep_nameB]['size']:
        
            # Make A the size of A U B
            self.sets[rep_nameA]['size'] += self.sets[rep_nameB]['size']
            
            # Set B's set name to that of A
            self.sets[rep_nameB]['name'] = rep_nameA
        else:
            # Do the converse
            self.sets[rep_nameB]['size'] += self.sets[rep_nameA]['size']
            self.sets[rep_nameA]['name'] = rep_nameB
    
    def find(self, data_point):
        """Find the set that a particular data point belongs to."""
        set_name = data_point
        visited = set()    
        while self.sets[set_name]['name'] != None:
            if set_name in visited:
                print("Cycle detected:", visited)
                break
            visited.add(set_name)
            set_name = self.sets[set_name]['name']
        return set_name


def demo():
    """Clustering demo. Run from package root."""
    
    # Initialize sets as disjoint singletons
    with open('examples/items.csv', 'r') as items:
        reader = csv.DictReader(items)
        uf = UnionFind(row['item'] for row in reader)
        # ^^ make these integers if doing it for real
    
    # Cluster equivalent items
    with open('examples/equivalent_items.csv', 'r') as equivalent_items:
        reader = csv.DictReader(equivalent_items)
        for row in reader:
            uf.union(row['item1'], row['item2'])
    
    # Output clusters
    with open('examples/item_clusters.csv', 'w') as item_clusters:
        writer = csv.writer(item_clusters)
        writer.writerow(['item', 'cluster'])
        writer.writerows([item, uf.find(item)] for item in uf.sets)


if __name__ == '__main__':
    demo()

