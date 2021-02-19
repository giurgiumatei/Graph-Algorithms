from Domain import *
from UI import *
import copy
from random import *



def graph_from_random(verticex,edges):# function that generates a random graph
    inbound={}
    outbound={}
    vertices=[]
    cp=int(copy.deepcopy(edges))

    for i in range (0,verticex):
        
        if i not in vertices:
            vertices.append(copy.deepcopy(i))
            inbound[copy.deepcopy(i)]=[]
            outbound[copy.deepcopy(i)]=[]
        if cp>0:
            nr_of_edges=randint(0,int(cp/2)+1)
            cp-=nr_of_edges

            while nr_of_edges>0:
                
                j=randint(0,int(verticex))
                weight=randint(-100,100)
            
            
            
            
                if j not in vertices:
                    vertices.append(copy.deepcopy(j))
                    inbound[copy.deepcopy(j)]=[]
                    outbound[copy.deepcopy(j)]=[]
            
                outbound[copy.deepcopy(i)].append([copy.deepcopy(j),copy.deepcopy(weight)])
                inbound[copy.deepcopy(j)].append([copy.deepcopy(i),copy.deepcopy(weight)])
                nr_of_edges-=1

    
    
    graph=Directed_Graphs(inbound,outbound,vertices,verticex,edges)

    return graph
        
        


def graph_from_text_file():# function that reads a graph from a text file
    inbound={}
    outbound={}
    vertices=[]

    with open(r'C:\Users\giurg\OneDrive\Facultate\Grafuri\Lab1\graph10k.txt','r') as f: #change path here if you want to read from a different text file
        reader=f.readline()
        reader=reader.strip("\n")
        line=reader.split(' ')
        nr_of_vertices=line[0]
        nr_of_edges=line[1]

        reader = f.readline()
        reader=reader.strip("\n")
        line=reader.split(' ')

        if line[0] not in vertices:
            vertices.append(copy.deepcopy(line[0]))
            inbound[copy.deepcopy(line[0])]=[]
            outbound[copy.deepcopy(line[0])]=[]
        if line[1] not in vertices:
            vertices.append(copy.deepcopy(line[1]))
            inbound[copy.deepcopy(line[1])]=[]
            outbound[copy.deepcopy(line[1])]=[]
        
        outbound[copy.deepcopy(line[0])].append([copy.deepcopy(line[1]),copy.deepcopy(line[2])])
        inbound[copy.deepcopy(line[1])].append([copy.deepcopy(line[0]),copy.deepcopy(line[2])])



        while reader:
            reader = f.readline()
            if reader!="":
                reader=reader.strip("\n")
                line=reader.split(' ')
                if line[0] not in vertices:
                    vertices.append(copy.deepcopy(line[0]))
                    inbound[copy.deepcopy(line[0])]=[]
                    outbound[copy.deepcopy(line[0])]=[]
                if line[1] not in vertices:
                    vertices.append(copy.deepcopy(line[1]))
                    inbound[copy.deepcopy(line[1])]=[]
                    outbound[copy.deepcopy(line[1])]=[]
        
                outbound[copy.deepcopy(line[0])].append([copy.deepcopy(line[1]),copy.deepcopy(line[2])])
                inbound[copy.deepcopy(line[1])].append([copy.deepcopy(line[0]),copy.deepcopy(line[2])])

    graph=Directed_Graphs(inbound,outbound,vertices,nr_of_vertices,nr_of_edges)

    return graph

def write_to_file(graph):# function that writes the graph to the text file

    with open(r'C:\Users\giurg\OneDrive\Facultate\Grafuri\Lab1\results.txt','w') as f:#change path here if you want to write to a different text file
        inbound=graph.get_outbound()
        f.write(str(graph.get_number_of_vertices())+" "+str(graph.get_number_of_edges())+'\n')

        for i in inbound:
            for j in inbound[i]:
                f.write(str(i)+' '+str(j[0])+ ' '+str(j[1])+'\n')





def main():# program starts with this function

    print("1.Read a graph from the text file")
    print("2.Generate a random graph")
    
    while True:
        try:
            op=int(input())
            assert op==1 or op==2
            break
        except:print("Give a valid option! ")

    if op ==1:
        graph=graph_from_text_file()
        write_to_file(graph)
    elif op==2:
        vertices=int(input("Give the number of vertices "))
        edges=int(input("Give the number of edges "))

        graph=graph_from_random(vertices,edges)
    
    ui=UI(graph)

    ui.start()
    write_to_file(graph)

    


if __name__ == '__main__':# program starts here
    main()