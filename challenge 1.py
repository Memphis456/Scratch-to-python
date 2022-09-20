name = (input("What is your name?: "))

print("Hello", name)

shape = input("What shape would you like me to draw for you?: ").lower() 
if shape == "square":
    print(" ______________")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
if shape == "circle":
    print("         , - ~ ~ ~ - ,")
    print("     , '               ' ,")
    print("   ,                       ,")
    print("  ,                         ,")
    print(" ,                           ,")
    print(" ,                           ,")
    print(" ,                           ,")
    print("  ,                         ,")
    print("   ,                       ,")
    print("     ,                  , '")
    print("       ' - , _ _ _ ,  '")

if shape == "triangle":
    print("       /\ ")
    print("      /  \ ")
    print("     /    \ ")
    print("    /      \ ")
    print("   /        \ ")
    print("  /          \ ")
    print(" /            \ ")
    print("/______________\ ")
                

