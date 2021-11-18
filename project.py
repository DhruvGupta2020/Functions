x = open("text1.txt")

d = x.read()

p = open("text2.txt")

l= p.read()

z = open("text1.txt","w")

m = open("text2.txt","w")

z.write(l)
m.write(d)
