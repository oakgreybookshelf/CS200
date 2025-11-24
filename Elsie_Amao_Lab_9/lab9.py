'''
CSIT-200
Elsie Amao
'''

# A C G H T
def adj_matrix():
    mat = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    
    return mat

def find_degree(vertex):
    mat = adj_matrix()
    total = 0
    if (vertex == 'A') or (vertex == 'a'):
        for num in mat[0]:
            total += num
    
    elif (vertex == 'C') or (vertex == 'c'):
        for num in mat[1]:
            total += num
    
    elif (vertex == 'G') or (vertex == 'g'):
        for num in mat[2]:
            total += num
    
    elif (vertex == 'H') or (vertex == 'h'):
        for num in mat[3]:
            total += num
    
    elif (vertex == 'T') or (vertex == 't'):
        for num in mat[4]:
            total += num
    
    return total

def find_neighborhood(vertex):
    pass
'''
neighbors = []
for i in range(5):
    if matrix[3][i] != 0:
        neighbors.append(i)
# neighbors now contains all vertices connected to 3
'''
def find_path(matrix, source_vertex, destination_vertex, answer):
    nodes = ['A', 'C', 'G', 'H', 'T']
    sv = source_vertex
    dv = destination_vertex
    '''
    if sv == 'A':
        for num in mat[0]:
            if mat[0][1] = dv:
                answer.append(dv)
    for list in mat:
        for value in mat[list]:
            if value[1] == dv:
                dv = list
                answer.append(dv)
            else:
    '''
    #copy = matrix
    while matrix:
        if answer != []:
            if dv == nodes.index(answer[-1]):
                #del answer[0]
                return answer
        else:
            for j in matrix[sv]:
                #print(matrix[sv].index(j), j) #index([j])
                if j == 1:
                    if matrix[sv].index(j) == dv:
                        answer.append(nodes[dv])
                        return answer
        answer.append(nodes[sv])
        if matrix != []:
            matrix.remove(matrix[sv])
        find_path(matrix, sv + 1, dv, answer)

    return answer



def main():

    print(adj_matrix())

    Y = "Y"

    while Y == "Y":
        print("""
Choose an action from the menu:
1. Find degree
2. Find neighborhood
3. Find path
                """)
        
        choice = input("Enter your choice: ")

        if choice == "1":
            vertex = input("Enter the vertex you want the degree of: ")
            print("The degree of vertex", vertex, "is", find_degree(vertex))
        elif choice == "2":
            pass 
        elif choice == "3":
            source = input("Enter the the source vertex: ")
            destination = input("Enter the the destination vertex: ")

            if source == 'A' or source == 'a':
                source = 0
            elif source == 'C' or source == 'c':
                source = 1
            elif source == 'G' or source == 'g':
                source = 2
            elif source == 'H' or source == 'h':
                source = 3
            elif source == 'T' or source == 't':
                source = 4

            if destination == 'A' or destination == 'a':
                destination = 0
            elif destination == 'C' or destination == 'c':
                destination = 1
            elif source == 'G' or destination == 'g':
                destination = 2
            elif destination == 'H' or destination == 'h':
                destination = 3
            elif destination == 'T' or destination == 't':
                destination = 4

            matrix = adj_matrix()
            nodes = ['A', 'C', 'G', 'H', 'T']
            answer = [nodes[source]]
            print("The path is", find_path(matrix, source, destination, []))
        else:
            print("Please enter a number between 1 and 3")
        
        Y = input("Do you want to continue (Y or N): ")

if __name__ == "__main__":
    main()