# https://www.geeksforgeeks.org/__name__-special-variable-python/
# nameWithValueMainExample1.py

print "nameWithValueMainExample1 __name__ = %s" %__name__

if __name__ == "__main__":
    print "nameWithValueMainExample1 is being run directly"
else:
    print "nameWithValueMainExample1 is being imported"
