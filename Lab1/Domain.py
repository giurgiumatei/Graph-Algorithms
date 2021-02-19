

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

    def set_vertices(self,new_vertices):# setter for the list of vertices
        self.vertices=new_vertices
    
    def is_edge(self,source_vertex,target_vertex):#checks if there is an edge 
                                                  #from source_vertex to target_vertex
        
        vertices=self.outbound[source_vertex]

        for i in vertices:
            if i[0] == target_vertex:
                return True 

        return False

    def get_in_degree(self,vertex):# returns the in degree of a given vertex

        return len(self.inbound[vertex])

    def get_out_degree(self,vertex):# returns the out degree of a given vertex

        return len(self.outbound[vertex])

    def iterate_outbound_edges(self,vertex):# prints the outbound edges of a given vertex

        for i in self.outbound[vertex]:
            print(i[0])

    def iterate_inbound_edges(self,vertex):#prints the inbound edges of a given vertex

        for i in self.inbound[vertex]:
            print(i[0])

    
    def modify_weight(self,source_vertex,target_vertex,new_weight):# modifies the weight of an edge

        vertices=self.outbound[source_vertex]

        for i in vertices:
            if i[0] == target_vertex:
                i[1]=new_weight

        
        self.outbound[source_vertex]=vertices

    def retrieve_weight(self,source_vertex,target_vertex):# returns the weight of an edge

        vertices=self.outbound[source_vertex]

        for i in vertices:
            if i[0] == target_vertex:
                return i[1]


    def add_vertex(self,vertex): #adds a new vertex to the graph

        self.vertices.append(vertex)
        self.number_of_vertices+=1

    
    
    def remove_vertex(self,vertex):# deletes a vertex from the graph
        self.vertices.remove(vertex)
        del self.inbound[vertex]
        del self.outbound[vertex]

        inbound_vertices=self.inbound.copy()

        for i in inbound_vertices:
            for j in inbound_vertices[i]:
                if j[0] == vertex:
                    self.inbound[i].remove(j)

        
        outbound_vertices=self.outbound.copy()

        for i in outbound_vertices:
            for j in outbound_vertices[i]:
                if j[0] == vertex:
                    self.outbound[i].remove(j)
        self.number_of_vertices-=1
        

    
    
    def add_edge(self,source_vertex,target_vertex,weight):# adds an edge to the graph

        vertices=self.outbound[source_vertex]
        vertices.append([target_vertex,weight])
        self.outbound[source_vertex]=vertices
        
        vertices=self.inbound[target_vertex]
        vertices.append([source_vertex,weight])
        self.inbound[target_vertex]=vertices

        

    def remove_edge(self,source_vertex,target_vertex):# removes an edge from the graph

        outbound_vertices=self.outbound[source_vertex]

        for j in outbound_vertices:
            if j[0] == target_vertex:
                self.outbound[source_vertex].remove(j)

        inbound_vertices=self.inbound[target_vertex]

        for j in inbound_vertices:
            if j[0] == source_vertex:
                self.inbound[target_vertex].remove(j)

    

        


    


        

       




        

       















            






        




        
        



    

