from pyjavaproperties import Properties

p_file=Properties()
p_file.load(open("./../config.properties"))

value=p_file["ITO"]

print(p_file.items()) # to print all the values in prop file ; it will print this in dict pattern

print(value)
print(type(value))