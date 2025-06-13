

m=[
["A", "B", "C"],
["D", "E", "F"],
["G", "H", "I"]
]

while True:
    print("Quieres ejecutar la Matriz")
    print("1. Si")
    print("2. No")



for f in m:
    for c in f:
        if c == "C":
            print("Esta en la matriz la letra: ", c)