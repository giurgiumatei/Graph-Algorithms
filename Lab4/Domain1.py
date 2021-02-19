from copy import deepcopy
from sys import maxsize
class Directed_Graphs: #the directed graph class

    def __init__(self,outbound,vertices,number_of_vertices,number_of_edges):

        self.number_of_vertices=number_of_vertices # this variable stores the number of vertices of the graph
        self.number_of_edges=number_of_edges# this variable stores the number of vertices of the graph
        self.outbound=outbound# this is a dictionary storing the outbound edges for every vertex
        self.vertices=vertices# this is a list containing every vertex of the graph

    def get_number_of_vertices(self): # returns the number of vertices of the graph
        return self.number_of_vertices

    def get_number_of_edges(self):# returns the number of edges of the graph
        return self.number_of_edges

    
    def get_vertices(self):# returns the list of vertices of the graph
        return self.vertices
    
    def get_outbound(self):# returns the dictionary of outbound edges
        return self.outbound

    def retrieve_weight(self,source_vertex,target_vertex):# returns the weight of an edge

        

        vertices=self.outbound[source_vertex]

        for i in vertices:
            if i[0] == target_vertex:
                return int(i[1])



    def minKey(self, key, mstSet): 
  
        # Initilaize min value
         
        minimum = int(maxsize)
  
        for vertex in self.vertices: 
            
            if int(key[vertex]) < minimum and mstSet[vertex] == False: 
                minimum = int(key[vertex]) 
                min_index = vertex 
  
        return min_index 
    
    
    
    
    
    def Prim(self,source_point): 
        
        #maxsize=9999999
        # Key values used to pick minimum weight edge in cut 

        key={}
        parent={}
        mstSet={}
        for v in self.vertices:

            key[v] = int(maxsize)  
            parent[v] = None  # Array to store constructed MST 
            mstSet[v]=False
        
        key[source_point] = 0 # Make key 0 so that this vertex is picked as first vertex 
        
  
        parent[source_point] = -1 # First node is always the root of 
  
        for mock_variable in self.vertices: 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # next_vertex is always equal to source_point in first iteration 
            next_vertex = self.minKey(key, mstSet) 
            
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[next_vertex] = True
            
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for vertex in self.outbound[next_vertex]: 
                # mstSet[vertex[0]] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if mstSet[vertex[0]] == False and int(key[vertex[0]]) > int(vertex[1]): 
                        key[vertex[0]] = vertex[1]
                        parent[vertex[0]] = next_vertex

        cost=0
        solution=[]
        for i in self.vertices:
            if parent[i] != -1:
                edge=[parent[i],i]
                edge.sort()
                solution.append(edge)
                cost+=int(key[i])
        print(cost)
        return solution
        
