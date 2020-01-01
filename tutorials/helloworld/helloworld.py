print("Welcome to the Python !")

if 5 > 2:
    print("Five is greater than two!") 

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a_array = ["A", "B", "c", "D", "E", "F", "G", "H"]
print(a_array) 

for x in a_array:
    print(x)

if "A" in a_array:
    print("Yes, 'A' is in the fruits list")

print(len(a_array))

def helloWrold(_argument):
	print("Welcome to the world of "+_argument)

helloWrold("Python")

def my_function(*kids): 
    print("The youngest child is " + kids[2]) 
 
my_function("Emil", "Tobias", "Linus")
