'''
CSIT-200
Elsie Amao
'''

def adj_matrix():
    '''
    matrix = [[0] * V for _ in range(V)]

    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1
    '''
    mat = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    '''
    mat = [[0] * 5 for _ in range(5)]
    mat['A']['C'] = 1
    mat['C']['A'] = 1

    mat['C']['G'] = 1
    mat['G']['H'] = 1
    mat['H']['T'] = 1
    mat['T']['A'] = 1
    mat['T']['G'] = 1
    '''
    return mat

    #mat = [[0, 15, 0, 7, 10, 0], [15, 0, ...], [...], [...]]
#m[0][1]  # = 15 (weight of 1-2)

    return matrix

def find_degree(vertex):
    mat = adj_matrix()
    total = 0
    if vertex == 'A':
        for num in mat[0]:
            total += num
    
    elif vertex == 'C':
        for num in mat[1]:
            total += num
    
    elif vertex == 'G':
        for num in mat[2]:
            total += num
    
    elif vertex == 'H':
        for num in mat[3]:
            total += num
    
    elif vertex == 'T':
        for num in mat[4]:
            total += num
    
    return total

def find_neighborhood(vertex):
    pass

def find_path(source_vertex, destination_vertex):
    pass


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
            print(find_degree(vertex))
        elif choice == "2":
            pass 
        elif choice == "3":
            pass
        else:
            print("Please enter a number between 1 and 3")
        
        Y = input("Do you want to continue (Y or N): ")

if __name__ == "__main__":
    main()