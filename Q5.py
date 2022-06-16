def factorial(n):
   counter = 1
   total = n
   while counter < n:
       total *= (n-counter)
       counter += 1
   return total

print(factorial(3)) #should print 6