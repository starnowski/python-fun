

### TODO Right tests
def fun1(): # Definition starts always (I guess) with colon ":"
    print("I am your first function")

fun1() #Direct invocation of function, on standard output we should see printed line "I am your first function"
print(fun1()) #Direct invocation of function but in "print" statement, now because our function does not returen any thing (I think you can say that it returns "None") then on console  we will see "I am your first function" and second line below with statement "None"
print(fun1) #In this case you just prints function object, like in java when you prints array object by simpling passing array object to system.out , int a[] = new int[]{10};System.out.println(a);