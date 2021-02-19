from Domain import *
from copy import deepcopy

class UI:

    def __init__(self,graph):#the UI is initialised with the graph
        self.graph=graph


    def print_menu(self): # prints the menu

        print("11.Represent the graph using the set of inbound edges: ")
        print("12.Represent the graph using the set of outbound edges: ")
        print("13.Find out the smallest path from node A to node B: ")

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

        destination_point=input("Give the destination node: ")

        print(vertices)
        if source_point not in vertices or destination_point not in vertices:
            print("Invalid input! ")

        else:
            result=self.graph.BFS(source_point,destination_point)
            if result!=None:
                print(result[0])
                print("Length is "+str(result[1]))
            else:
                print("There is no path! ")

            
