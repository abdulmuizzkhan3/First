# best friends: strings and lists
# to find the spaces and split it into pieces.
# And there is a built-in function in Python called split.
# so abc.split, and this returns a list.
# So it basically takes a string and gives us back a list.
# And the list is with three words. The spaces are gone, they're chopped up
abc='with three words'
stuff=abc.split()
print(stuff)

print(len(stuff))
print(stuff[0])
print(stuff)

for w in stuff:
    print(w)

# other examples
line=" a lot                 of spaces"
etc=line.split()
print(etc)

line="first;second;third"
thing=line.split(";")
print(len(thing))
print(thing)
