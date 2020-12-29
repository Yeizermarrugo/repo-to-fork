#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


def fib(n):
    a, b = 0,1
    while a < n:
        print(a)
        a, b = b, a + b


# In[8]:


def primos(n):
    numbers = [True, True] + [True] * (n-1)
    last_prime_number = 2
    i = last_prime_number
    
    while last_prime_number**2 <= n:
        i += last_prime_number
        while i <= n:
            numbers[i] = False
            i += last_prime_number
        j = last_prime_number + 1
        while j < n:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number
    
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]


# In[34]:


def perfecto(num):

    suma = 0

    for i in range(1, num):
        #print(i)

        if num % i == 0:
            suma = suma + i

    if (suma == num):

        return True

    else:

        return False


# In[45]:


def numeros_perfectos(n):
    factors = []
    i = 1
    while len(factors) != n:
        if perfecto(i):
            factors.append(i)
        i += 1
    return factors


# In[48]:


numeros_perfectos(3)
primos(10)
fib(10)


# In[ ]:




