#.format 
st = "{},{},{}".format ("Hello","my name is Mikalai", "how you doing?")
print (st)
#f
var1 = 123
var2 = 456
print (f"{var1}, {var2}")
#cap, upper,lower, title, len - длинна строки, 
print ("hello mike".capitalize())
print ("hello".upper())
print ("HELLO".lower())
print ("hello mike".title())
print (len("hello, im mike"))
#split, join, replace, startswith, endswith, find, index
print ("asd, fgh, akl".split('a'))
print ("asd".join(["dff","ghh"]))
print ("asd".replace("a","F"))
print ("asd".startswith("has"))
print ("asd".endswith("d"))
print ("asd".find("d"))
print ("asgtbbrgnd".index("n"))
#lists
expl_list = ["miko, kar, misha, egor".title()]
expl_list1 = [1,2,3,4]
print(expl_list + expl_list1)
print (expl_list1 * 3)
print (len(expl_list1 * 3))
expl_list1.insert(1, 12)
print(expl_list1)
expl_list1.append("asd")
print(expl_list1)
expl_list.append(expl_list1)
print(expl_list)
expl_list.extend(expl_list1)
print(expl_list)
print(expl_list1[:3])