# Lab | Numpy Deep Dive

## #1 
**Import the NUMPY package under the name np** 

Used the following code in Python:
```
import numpy as np
```


## #2 
**Print the NUMPY version and the configuration.**

Used the following code in Python to get the version:
```
print(np.version.version) 
```
```
Output:
1.15.2
```
Used the following code in Python to get the configuration:
```
print(np._config_.show())
```

## #3
**Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a".**

Used the following code in Python:
```
a = np.random.random((2,3,5)) 
```
This created an array with two groups of 3 x 5 matrices.


## #4
**Print a.**

Used the following code in Python:
```
print(a)
```


## #5
**Create a 5x2x3 3-dimensional array with all values equaling 1. Assign the array to variable "b"**

Used the following code in Python:
```
lst = [[(1,1,1),(1,1,1)],[(1,1,1),(1,1,1)],[(1,1,1),(1,1,1)],[(1,1,1),(1,1,1)],[(1,1,1),(1,1,1)]]

b = np.array(lst)
```
This created an array with five groups of 2 x 3 matrices.


## #6
**Print b.**

Used the following code in Python:
```
print(b)
```


## #7
**Do a and b have the same size? How do you prove that in Python code?**

a and b do not have the same size, to prove it, I used the following code in Python:

### Attempt 1

Used the following code in Python:
```
print(a.size)
print(b.size)
```
```
Output:
30
30
```
Using the size command returned the same table size, which is incorrect.
The size command just multiplies the elements of the shape, therefore since both arrays have the same numbers, it seems like they have the same size.

### Attempt 2

Used the following code in Python:
```
print(a.shape)
print(b.shape)
```
```
Output:
(2,3,5)
(5,2,3)
```
Using the shape command shows that the arrays have differnet sizes. 


## #8
**Are you able to add a and b? Why or why not?**

No because they have different shapes, when executing the following code in Python, an error occurs. 
```
print(np.add(a, b))
```

## #9
**Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".**

Used the following code in Python:
```
c = np.transpose(b,(1,2,0))
```
or
```
c = np.reshape(b,(2,3,5))
```

## #10
**Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?**

Used the following code in Python:
```
d = np.add(a, c)
print(d)
```
It works now because both arrays have the same shape.

## #11 
**Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.**

Used the following code in Python:
```
print(a)
print(d)
```
Items in array d are larger by 1 because array d is adding the random number from array a with the 1 from array b.


## #12
**Multiply a and c. Assign the result to e.**

Used the following code in Python:
```
e = np.multiply(a,c)
```


## #13
**Does e equal to a? Why or why not?**

Used the following code in Python:
```
e == a
```
Yes, because array e is multiplying the random numbers in array a by 1. To prove this, I used the boolean evaluator == as shown above.


## #14
**Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"**

Used the following code in Python:
```
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
```
Solution in class with Marc:
```
d_data = (np.min(d), np.max(d), np.mean(d))
(min,max,mean) = d_data
```

## #15
**Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.**

Used the following code in Python:
```
f = np.empty((2,3,5))
```


## #16
**Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.**

Used the following code in Python:
```
for a0, block in enumerate(d):
     for a1, line in enumerate(block):
         for a2, column in enumerate (line):
             if d[a0,a1,a2] == d_mean:
                    f[a0,a1,a2] = 50
             if d[a0,a1,a2] == d_max:
                    f[a0,a1,a2] = 100
             if d[a0,a1,a2] == d_min:
                    f[a0,a1,a2] = 0
             if (d[a0,a1,a2] > d_min) and (d[a0,a1,a2] < d_mean):
                    f[a0,a1,a2] = 25
             if (d[a0,a1,a2] > d_mean) and (d[a0,a1,a2] < d_max):
                    f[a0,a1,a2] = 75
```
Solution in class with Marc:
```
d_min = (d != min) * d OR d_min = np.zeroes(d.shape)
d_min_mean = (d > min) * (d < mean) * 25
d_mean = (d == mean) * 50
d_max_mean = (d < max) * (d > mean) * 75
d_max = (d == max) * 100
print(d_min + d_min_mean + d_mean + d_max_mean + d_max)
```
```
f = np.empty((2,3,5))
f[d<d_mean]=25
f[d>d_mean]=75
f[d==d_min]=0
f[d==d_mean]=50
f[d==d_max]=100
```


## #17
**Print d and f. Do you have your expected f?**

Used the following code in Python:
```
print(d)
print(f)
```