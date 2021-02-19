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

    def retrieve_weight(self,source_vertex,target_vertex):# returns the weight of an edge

        vertices=self.inbound[source_vertex]

        for i in vertices:
            if i[0] == target_vertex:
                return i[1]

        return None



    def Dijkstra(self,starting_vertex,destination_vertex):

        copy_starting_vertex=deepcopy(starting_vertex) #copy of starting vertex

        pqueue=[] #the priority que

        previous={} #dictionary of previous node of a given key

        distance={} #distance from the starting vertex

        pqueue.append((0,starting_vertex)) #priority queue with node and priority

        distance[starting_vertex]=0 #distance from the starting vertex

        found=False #if true exit while loop

        while pqueue and found == False:

            copy_vertex=pqueue.pop(0) #copy vertex from head of queue
            
            
            for i in self.inbound[copy_vertex[1]]:
                
                if i[0] not in distance or (int(distance[copy_vertex[1]])+ int(self.retrieve_weight(copy_vertex[1],i[0])))<distance[i[0]]:
                    
                    distance[i[0]]=int(distance[copy_vertex[1]])+int(self.retrieve_weight(copy_vertex[1],i[0]))
                    pqueue.append((self.retrieve_weight(copy_vertex[1],i[0]),i[0]))
                    pqueue.sort(reverse=True) #pqueue is in correct order
                    previous[i[0]]=copy_vertex[1]

            if copy_vertex==destination_vertex:
                found=True

       
        path=[]

        node=destination_vertex

        path.append(deepcopy(node))
        
        length=0


        while node!=copy_starting_vertex: #build the path to node
            try:
                node=previous[node]
                length+=distance[destination_vertex]
                print(length)
            except:
                
                return
            path.append(deepcopy(node))
            

        

        result=[]
        result.append(path)
        result.append(distance[destination_vertex])

        return result
            

                    


