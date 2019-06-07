# Should not be able to compile

# Expected error:
# Traceback (most recent call last):
# ..., line 3, in <module>
# print("some string " + 12)
# TypeError: cannot concatenate 'str' and 'int' objects

#TODO Add unit test which execute python from python and check python interperter output

print("some string " + 12)