def de_uma_vez():
    f = open("words.txt")

    l = f.readlines()

    print(type(l))
    print(len(l))
    print(l)

def uma_a_uma():
    f = open("words.txt")

    for l in f:
        print(type(l))
        print(l)

def so_a_primeira_e_segunda():
    f = open("words.txt")

    l = f.readline()

    print(type(l))
    print(l)

    l = f.readline()

    print(type(l))
    print(l)

def numa_so_string():
    f = open("words.txt")

    l = f.read()

    print(type(l))
    print(len(l))
    print(l)


de_uma_vez()
#uma_a_uma()
#so_a_primeira_e_segunda()
print("====")
numa_so_string()
