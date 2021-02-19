from copy import deepcopy

class Directed_Graphs: #the directed graph class

    def __init__(self,inbound,outbound,vertices,number_of_vertices,number_of_edges):

        self.number_of_vertices=number_of_vertices # this variable stores the number of vertices of the graph
        self.number_of_edges=number_of_edges# this variable stores the number of vertices of the graph
        self.inbound=inbound# this is a dictionary storing the inbound edges for every vertex
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



    def BFS(self,starting_vertex,destination_vertex):

        copy_starting_vertex=deepcopy(starting_vertex)

        visited_nodes=[]

        queue=[]

        distance={}
        previous={}

        queue.append(deepcopy(starting_vertex))
        
        visited_nodes.append(deepcopy(starting_vertex))
        distance[starting_vertex]=0

        while queue:

            starting_vertex=queue.pop(0)

            
            for i in self.outbound[starting_vertex]:
                if i[0] not in visited_nodes:
                    queue.append(deepcopy(i[0]))
                    visited_nodes.append(deepcopy(i[0]))
                    distance[i[0]]=distance[starting_vertex]+1
                    previous[i[0]]=starting_vertex

        
        path=[]

        node=destination_vertex

        path.append(deepcopy(node))
        
        
        while node!=copy_starting_vertex:
            try:
                node=previous[node]
            except:
                
                return
            path.append(deepcopy(node))
            

        path.reverse()

        result=[]
        result.append(path)
        result.append(len(path)-1)

        return result



            

