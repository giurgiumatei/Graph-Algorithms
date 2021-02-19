from Domain1 import *
from copy import deepcopy

class UI:

    def __init__(self,graph):#the UI is initialised with the graph
        self.graph=graph


    def print_menu(self): # prints the menu

       # print("11.Represent the graph using the set of inbound edges: ")
        print("12.Represent the graph using the set of outbound edges: ")
        print("13.Find a minimal spanning tree: ")

    def start(self): # UI starts here

        while True:
            self.print_menu()

            while True:
                try:
                    op=int(input())
                    assert op>=11 and op<=13 or op==0
                    break
                except:print("Give a valid option! ")


        # op stores the option chosen by the user and using the following if statements
        # will help execute the afferent method
            if op == 0:
                break

            elif op==11:
                self.option11()
            elif op==12:
                self.option12()
            elif op==13:
                self.option13()
            
    
    def option11(self):
    
        print(self.graph.inbound)
    

    def option12(self):
    
        print(self.graph.outbound)

    def option13(self):
        
        
        vertices=self.graph.get_vertices()

        source_point=input("Give the starting node: ")

        
        
        if source_point not in vertices:
            print("Invalid input! ")

        else:
            
           
            solution=self.graph.Prim(source_point)
            solution.sort()
            solutions=[]
            solutions.append(solution)
           
            for i in solution:
                print(i[0], "-", i[1])
            print("\n")
            another_solution=[]

            for vertex in self.graph.vertices:
                another_solution=self.graph.Prim(vertex)
                another_solution.sort()

                if another_solution not in solutions:
                    for i in another_solution:
                        print(i[0], "-", i[1])
                    print("\n")

                
                