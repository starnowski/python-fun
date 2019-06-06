# https://www.geeksforgeeks.org/__name__-special-variable-python/

import nameWithValueMainExample1

print "nameWithValueMainExample2 __name__ = %s" %__name__

if __name__ == "__main__":
    print "nameWithValueMainExample2 is being run directly"
else:
    print "nameWithValueMainExample2 is being imported"
