from Domain import *
from copy import deepcopy

class UI:

    def __init__(self,graph):#the UI is initialised with the graph
        self.graph=graph


    def print_menu(self): # prints the menu

        print("1.Get the number of vertices: ")
        print("2.Iterate the set of vertices: ")
        print("3.Find out whether there is an edge from the first one to the second one: ")
        print("4.Get the in degree and the out degree of a specified: ")
        print("5.Iterate the set of outbound edges of a specified vertex: ")
        print("6.Parse the set of inbound edges of a specified vertex: ")
        print("7.Retrieve the information (the integer) attached to a specified edge: ")
        print("8.Modify the information (the integer) attached to a specified edge: ")
        print("9.Modify the graph: ")
        print("10.Copy the graph: ")
        print("11.Represent the graph using the set of inbound edges: ")
        print("12.Represent the graph using the set of outbound edges: ")

    def start(self): # UI starts here

        while True:
            self.print_menu()

            while True:
                try:
                    op=int(input())
                    assert op>=0 and op<=12
                    break
                except:print("Give a valid option! ")


        # op stores the option chosen by the user and using the following if statements
        # will help execute the afferent method
            if op == 0:
                break

            elif op==1:
                self.option1()
            elif op==2:
                self.option2()
            elif op==3:
                self.option3()
            elif op==4:
                self.option4()
            elif op==5:
                self.option5()
            elif op==6:
                self.option6()
            elif op==7:
                self.option7()
            elif op==8:
                self.option8()
            elif op==9:
                self.option9()
            elif op==10:
                self.option10()
            elif op==11:
                self.option11()
            elif op==12:
                self.option12()
            
    def option1(self): #prints the number of vertices
        print(self.graph.get_number_of_vertices())
        

    def option2(self): # iterates the set of vertices

        print(self.graph.get_vertices())

    def option3(self): # tells if there is an edge from a source vertex to a target vertex

        sp=input("Give the source vertex: ")
        tp=input("Give the target vertex: ")

        if self.graph.is_edge(sp,tp)==True:
            print("Yes")
        else: print("No")

    def option4(self):# prints the in degree and the out degree of a specified vertex
        
        vertex=input("Give the vertex: ")
        in_dgr=self.graph.get_in_degree(vertex)
        out_dgr=self.graph.get_out_degree(vertex)

        print("The in degree of the vertex is " + str(in_dgr) + " and the out degree is "+str(out_dgr))

    def option5(self):# parses the set of outbound edges of a specified vertex
        vertex=input("Give the vertex: ")
        self.graph.iterate_outbound_edges(vertex)
        

    def option6(self):# parses the set of inbound edges of a specified vertex

        vertex=input("Give the vertex: ")
        self.graph.iterate_inbound_edges(vertex)
        

    def option7(self): #retrieves the weight of a specified edge

        sp=input("Give the source vertex: ")
        tp=input("Give the target vertex: ")
        print(self.graph.retrieve_weight(sp,tp))

    def option8(self): # modifies the weight of a specified edge

        sp=input("Give the source vertex: ")
        tp=input("Give the target vertex: ")
        weight=input("Give the new weight: ")
        self.graph.modify_weight(sp,tp,weight)

    def option9(self): #adds/removes a vertex or an edge

        
        print("1.Add a vertex: ")
        print("2.Remove a vertex: ")
        print("3.Add an edge: ")
        print("4.Remove an edge")

        while True:
            try:
                op=int(input())
                assert op>=1 and op<=4
                break
            except:print("Give a valid option! ")
        
        # op stores the option chosen by the user and using the following if statements
        # will help execute the afferent method

        if op==1:

            vertex=input("Give the new vertex")

            vertices=self.graph.get_vertices()

            if vertex not in vertices:
                self.graph.add_vertex(vertex)
            else: 
                print("Vertex already exists! ")

        elif op==2:

            vertex=input("Give the vertex to be removed")

            vertices=self.graph.get_vertices()

            if vertex in vertices:
                
                self.graph.remove_vertex(vertex)
            else: 
                print("Vertex does not exist! ")

        elif op==3:

            sp=input("Give the source vertex: ")
            tp=input("Give the target vertex: ")
            weight=input("Give the weight: ")

            self.graph.add_edge(sp,tp,weight)
        
        elif op==4:

            sp=input("Give the source vertex: ")
            tp=input("Give the target vertex: ")

            self.graph.remove_edge(sp,tp)

    def option10(self): #returns a deepcopy of the graph
        return deepcopy(self.graph)

    def option11(self):
    
        print(self.graph.inbound)
    

    def option12(self):
    
        print(self.graph.outbound)

    
            




            

            
            





