{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "77f6c16b",
   "metadata": {},
   "source": [
    "# python_function\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6412d239",
   "metadata": {},
   "outputs": [],
   "source": [
    "# # syntax\n",
    "# def function_name(parameter):\n",
    "#     \"\"\"doc string\"\"\"\n",
    "#     statement(s)\n",
    "#     return expression\n",
    "def fun():\n",
    "    print(\"well come to yarazari :\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "75c622aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "well come to yarazari :\n"
     ]
    }
   ],
   "source": [
    "fun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2393aad7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "well come to yarazari :\n"
     ]
    }
   ],
   "source": [
    "def fun():\n",
    "    print(\"well come to yarazari :\")\n",
    "fun() # dis code to call a function"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e91cfa03",
   "metadata": {},
   "source": [
    "# arguments of a function\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1e75212a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def evenodd(x):\n",
    "    if (x % 2) == 0 :\n",
    "        return \"even\"\n",
    "    else:\n",
    "        return \"odd\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0dcf679a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'odd'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evenodd(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "80e865d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'even'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evenodd(6)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c50250c",
   "metadata": {},
   "source": [
    "# types of arguments\n",
    "## python supports various types of arguments that can be passed at the time funcction call\n",
    "1. default arguments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9a4502ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(x,y=50):\n",
    "    print(\"x\",x)\n",
    "    print(\"y\",y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "69223389",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x 5\n",
      "y 50\n"
     ]
    }
   ],
   "source": [
    "myfun(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "def757cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(x=5,y=10):\n",
    "    return x,y,\"myfun is always to hack\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5db6b210",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 10, 'myfun is always to hack')"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myfun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ed30c7bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def student(fname,lname):\n",
    "    print(fname,lname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "aff8ff8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mahesh meti\n"
     ]
    }
   ],
   "source": [
    "student('mahesh','meti')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4f5e205d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def student(fname,lname):\n",
    "    return fname,lname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "eb7364bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('manjunath', 'kannur')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student('manjunath','kannur')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c9d790e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('manjunath', 'kannur')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student(fname = 'manjunath',lname = \"kannur\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4912bf4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('manjunath', 'kannur')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student(fname = \"manjunath\", lname = \"kannur\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa5cc707",
   "metadata": {},
   "source": [
    "# variable-length argements\n",
    "## *args (None-keyword arguments)\n",
    "## **kwargs (keyword arguments)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f2d4f7d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(*args):\n",
    "    for arg in args:\n",
    "        print(arg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "0fcaf52c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is akash\n",
      "25\n",
      "36\n",
      "89\n",
      "78\n",
      "45\n",
      "21\n",
      "36\n"
     ]
    }
   ],
   "source": [
    "myfun('my name is akash',25,36,89,78,45,21,36)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "baf3fc88",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(**kwargs):\n",
    "    for key,value in kwargs.items():\n",
    "        print(\"%s == %s\" %(key,value))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "13e52dc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "myfun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "117bc1f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fname == mahesh\n",
      "mid == low\n"
     ]
    }
   ],
   "source": [
    "myfun(fname = \"mahesh\",mid = \"low\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e425916",
   "metadata": {},
   "source": [
    "# docstring \n",
    "## the first string after the function is called the document string "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3a2e3cd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# this docstring describe the functionality of the funtion\n",
    "# print(functin_name.__doc__)\n",
    "# whether x is even or odd\n",
    "def evenodd(x):\n",
    "    \"\"\"function to check if the number is even or odd\"\"\"\n",
    "    if (x % 2 == 0):\n",
    "        return 'print even'\n",
    "    else:\n",
    "        return 'print odd'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a70884af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'print odd'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evenodd(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7f5da1e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'print even'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evenodd(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "93e0d7d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "function to check if the number is even or odd\n"
     ]
    }
   ],
   "source": [
    "print(evenodd.__doc__)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af1ac860",
   "metadata": {},
   "source": [
    "# the return statement\n",
    "## return [expression_list]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "83a2783f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def square(num):\n",
    "    return num**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "0c68afb3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "43adc5dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "print(square(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "83e252f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[20, 40, 50, 60, 70, 80, 90]\n"
     ]
    }
   ],
   "source": [
    "def myfun(x):\n",
    "    x[0] = 20\n",
    "lst = [30,40,50,60,70,80,90]\n",
    "myfun(lst)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "a41f8bea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 11, 12, 13, 14, 15]\n"
     ]
    }
   ],
   "source": [
    "def myfun(x):\n",
    "    x = [20,30,40]\n",
    "lst = [10,11,12,13,14,15]\n",
    "myfun(lst)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "72c4369a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "def myfun(x):\n",
    "    x = 20\n",
    "x = 10\n",
    "myfun(x)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e9787090",
   "metadata": {},
   "outputs": [],
   "source": [
    "def swap (x,y):\n",
    "    temp = x \n",
    "    x = y \n",
    "    y = temp\n",
    "    print(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "c9def438",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9 5\n"
     ]
    }
   ],
   "source": [
    "swap(5,9)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc409b26",
   "metadata": {},
   "source": [
    "# Anonymous function\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "81a537d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# an anonymous function means that a function is without a name\n",
    "# lambda keyword is used ot create anonymous function\n",
    "def cube(x):\n",
    "    return x*x*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "ad837e1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "125"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "c93f19fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "cube = lambda x : x*x*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "9ba048c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "125"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "780b6135",
   "metadata": {},
   "outputs": [],
   "source": [
    "cube = lambda x : x**3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "7581694b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "125"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "a64f7bb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "square = lambda x : x**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "f3d098d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "747b0254",
   "metadata": {},
   "outputs": [],
   "source": [
    "def square(x):\n",
    "    return x**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "6b0b8b26",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f919a43f",
   "metadata": {},
   "source": [
    "# python function within function\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "a719e357",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i love geeksforgeeks\n"
     ]
    }
   ],
   "source": [
    "# python that is defined inside another function is known as the inner function or nested function\n",
    "def f1():\n",
    "    s = \"i love geeksforgeeks\"\n",
    "    def f2():\n",
    "        print(s)\n",
    "    f2()\n",
    "f1()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bdbc9eae",
   "metadata": {},
   "source": [
    "# how to write an empty function in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "f488d987",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (Temp/ipykernel_1224/4039436457.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\yaraz\\AppData\\Local\\Temp/ipykernel_1224/4039436457.py\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    \u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "def fun():\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "50c7c86c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun():\n",
    "    pass  # it works dummy statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "0dc697b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "fun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "17eaa267",
   "metadata": {},
   "outputs": [],
   "source": [
    "# in python create pass statement\n",
    "def fun():\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d1965e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "mutex = True\n",
    "while (mutex == True):\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25dd72b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "if (mutex == True):\n",
    "    pass \n",
    "else:\n",
    "    print(\"False: \")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "daf081d7",
   "metadata": {},
   "source": [
    "# yield statement of return in python\n",
    "1. return: sends a specified value back to its caller \n",
    "2. yield : can produce a sequence of values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ac07b5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "# yield statement is suspended function return the value back to caller\n",
    "def simple():\n",
    "    yield 1\n",
    "    yield 2\n",
    "    yield 3\n",
    "for value in simple():\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1def0002",
   "metadata": {},
   "outputs": [],
   "source": [
    "def simple():\n",
    "    return 1,2,3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e5e4b318",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "simple()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ad86002e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def simple():\n",
    "    yield 1,2,3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "668392fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<generator object simple at 0x000001EC193417B0>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "simple()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2efaed30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3)\n"
     ]
    }
   ],
   "source": [
    "for value in simple():\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5adcb629",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nextsquare():\n",
    "    i = 1\n",
    "    while True:\n",
    "        yield i*i\n",
    "        i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2f454386",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n",
      "9\n",
      "16\n",
      "25\n",
      "36\n",
      "49\n",
      "64\n",
      "81\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "for num in nextsquare():\n",
    "    if num > 100:\n",
    "        break\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0605e56",
   "metadata": {},
   "source": [
    "# return multiple values in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "13544887",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'mack' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/1692971470.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# value from a method using class\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mclass\u001b[0m \u001b[0mmack\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"manjunath kannur\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/1692971470.py\u001b[0m in \u001b[0;36mmack\u001b[1;34m()\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mmack\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0mt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/1692971470.py\u001b[0m in \u001b[0;36mfun\u001b[1;34m()\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mmack\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m     \u001b[0mt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'mack' is not defined"
     ]
    }
   ],
   "source": [
    "# value from a method using class\n",
    "class mack:\n",
    "    def __init__(self):\n",
    "        self.str = \"manjunath kannur\"\n",
    "        self.x = 20\n",
    "def fun():\n",
    "    return mack()\n",
    "t = fun()\n",
    "print(t.str)\n",
    "print(t.x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9587b81b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun():\n",
    "    str = \"manjunathkannur\"\n",
    "    x = 20 \n",
    "    return x,str\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5c282baa",
   "metadata": {},
   "outputs": [],
   "source": [
    "str, x = fun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e93745d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "manjunathkannur\n"
     ]
    }
   ],
   "source": [
    "print(str)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "78d9cee5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['manjunathkannur: ', 20]\n"
     ]
    }
   ],
   "source": [
    "def fun():\n",
    "    str = \"manjunathkannur: \"\n",
    "    x = 20\n",
    "    return [str,x]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ab4a0152",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst = fun"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4411f667",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<function fun at 0x000002348CB2B940>\n"
     ]
    }
   ],
   "source": [
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5cbdb4ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst = fun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4118c84d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['manjunathkannur: ', 20]\n"
     ]
    }
   ],
   "source": [
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1ca9a89c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun():\n",
    "    d = dict()\n",
    "    d['str'] = 'geeksforgeeks'\n",
    "    d['x'] = 20\n",
    "    return d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "91c00be4",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = fun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "66d43db4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'str': 'geeksforgeeks', 'x': 20}\n"
     ]
    }
   ],
   "source": [
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06da9bc0",
   "metadata": {},
   "source": [
    "# partial function in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d473f6cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from functools import partial"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e7f0db51",
   "metadata": {},
   "outputs": [],
   "source": [
    "def f (a,b,c,d):\n",
    "    return 1000*a+1100*b+10*c+d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "47b3273d",
   "metadata": {},
   "outputs": [],
   "source": [
    "g = partial(f,2,5,6,8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "82d56370",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "functools.partial(<function f at 0x000002348CB2BC10>, 2, 5, 6, 8)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2c670396",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shout(text):\n",
    "    return text.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a22834f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO KANNUR\n"
     ]
    }
   ],
   "source": [
    "print(shout(\"hello kannur\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f7f54dd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "yella = shout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "dc43720e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.shout(text)>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yella"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "34abc2eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO KANNUR\n"
     ]
    }
   ],
   "source": [
    "print(yella(\"hello kannur\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "2126df72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KANNUR YELLA\n"
     ]
    }
   ],
   "source": [
    "print(yella(\"kannur yella\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "260b7979",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shout(text):\n",
    "    return text.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "691cfd4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def whisper(text):\n",
    "    return text.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "89b38f29",
   "metadata": {},
   "outputs": [],
   "source": [
    "def greet(func):\n",
    "    greeting = func(\"hi i am created by a function passed as an argument: \")\n",
    "    print(greeting)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "dd218737",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HI I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT: \n"
     ]
    }
   ],
   "source": [
    "greet(shout)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "20c55009",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi i am created by a function passed as an argument: \n"
     ]
    }
   ],
   "source": [
    "greet(whisper)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "55512255",
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_adder(x):\n",
    "    def adder(y):\n",
    "        return x+y\n",
    "    return adder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "36de581e",
   "metadata": {},
   "outputs": [],
   "source": [
    "add = create_adder(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "589390b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.create_adder.<locals>.adder(y)>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0089aed2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "print(add(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6068b8a8",
   "metadata": {},
   "source": [
    "# *args and **kwargs in Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "90e12060",
   "metadata": {},
   "outputs": [],
   "source": [
    "# *args (None-keyword arguments)\n",
    "# **kwargs (keyword arguments)\n",
    "def myfun(*argv):\n",
    "    for arg in argv:\n",
    "        print(arg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c0ca7a30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "wellcome\n",
      "to\n",
      "geeksforgeeks\n"
     ]
    }
   ],
   "source": [
    "myfun('hello','wellcome','to','geeksforgeeks')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "85bb2522",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(**kwargs):\n",
    "    for key , value in kwargs.items():\n",
    "        print(\"%s == %s\" %(key,value))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "84ca3e52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first == geeks\n",
      "mid == for\n",
      "last == geeks\n"
     ]
    }
   ],
   "source": [
    "myfun(first = 'geeks',mid ='for',last = 'geeks')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "38f07130",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(arg,arg1,arg2):\n",
    "    print(\"arg1: \",arg)\n",
    "    print(\"arg:\",arg1)\n",
    "    print(\"arg2\",arg2)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4b32dd8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "args = (\"geeks\",'for','geeks')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "790bd5ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "arg1:  geeks\n",
      "arg: for\n",
      "arg2 geeks\n"
     ]
    }
   ],
   "source": [
    "myfun(*args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "2904975c",
   "metadata": {},
   "outputs": [],
   "source": [
    "kwargs = {'arg':'geeks','arg1':'for','arg2':'geeks'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "0556729a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "arg1:  geeks\n",
      "arg: for\n",
      "arg2 geeks\n"
     ]
    }
   ],
   "source": [
    "myfun(**kwargs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "9a7d2d29",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(*args,**kwargs):\n",
    "    print(\"args: \",args)\n",
    "    print(\"kwargs: \",kwargs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f5b7a724",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(('geeks', 'for', 'geeks'), {'first': 'geeks', 'mid': 'for', 'last': 'geeks'})"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myfun ('geeks','for','geeks',first = 'geeks',mid = 'for',last='geeks')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "76b37826",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(*args,**kwargs):\n",
    "    return args,kwargs"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "978b3256",
   "metadata": {},
   "source": [
    "# python Closures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "5fa63d1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# befor seeing what a closure is A function that is defined inside another function is known as nested function\n",
    "def outer(text):\n",
    "    text = text\n",
    "    \n",
    "    def inner():\n",
    "        print(text)\n",
    "    inner()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "e122d08b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello renukadevi:\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    outer('hello renukadevi:')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "8003e3fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ptyhon Clousures\n",
    "def outer(text):\n",
    "    text = text\n",
    "    \n",
    "    def inner():\n",
    "        print(text)\n",
    "    return  inner   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "f4f3ebd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "renukadevi prasanna:\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    myfunction = outer('renukadevi prasanna:')\n",
    "    myfunction()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "797d8efb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import logging"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "6509ca53",
   "metadata": {},
   "outputs": [],
   "source": [
    "logging.basicConfig(filename = \"demo.log\",level = logging.INFO)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "60c38fbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def logger(func):\n",
    "    def log_func(*args):\n",
    "        logging.info('running \"{}\" with arguments'.format(func.__name__args))\n",
    "        print(func(*args))\n",
    "        return logic_func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "d22954f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(x,y):\n",
    "    return x+y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "bea5b4b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sub(x,y):\n",
    "    return x-y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "904828b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "add_logger = logger(add)\n",
    "sub_logger = logger(sub)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "ec2b5fed",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'NoneType' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/1808601744.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0madd_logger\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'NoneType' object is not callable"
     ]
    }
   ],
   "source": [
    "add_logger(4,3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ec1d585",
   "metadata": {},
   "source": [
    "# function Decorators in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "2033ac34",
   "metadata": {},
   "outputs": [],
   "source": [
    "# python function inside another function\n",
    "# python function can be passed as parameter to another function\n",
    "def message(str):\n",
    "    # nested function\n",
    "    def add():\n",
    "        return \"well come to: \"\n",
    "    return add() + str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "42f740dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def site(site_name):\n",
    "    return site_name\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "e6c9b112",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "well come to: manjunathkannur\n"
     ]
    }
   ],
   "source": [
    "print(message(site(\"manjunathkannur\")))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc59ec9f",
   "metadata": {},
   "source": [
    "# python Decorator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "6202e38b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def decorat(fun):\n",
    "    def add(site_name):\n",
    "        return \"wellcome to : \"+fun(site_name)\n",
    "    return add"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "5dd1fce2",
   "metadata": {},
   "outputs": [],
   "source": [
    "@decorat\n",
    "def site_name(site_name):\n",
    "    return site_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "d245ac14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'wellcome to : renukadevi prasanna: '"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "site_name(\"renukadevi prasanna: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "7ea48f50",
   "metadata": {},
   "outputs": [],
   "source": [
    "def att(func):\n",
    "    func.data = 3\n",
    "    return func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "20f57b44",
   "metadata": {},
   "outputs": [],
   "source": [
    "@att\n",
    "def add(x,y):\n",
    "    return x+y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "4ea3e4f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add(5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "8b08b1d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add.data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1bccfa1f",
   "metadata": {},
   "source": [
    "# Decorators in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "22162595",
   "metadata": {},
   "outputs": [],
   "source": [
    "# first class objects \n",
    "def shout(text):\n",
    "    return text.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "da340df4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO\n"
     ]
    }
   ],
   "source": [
    "print(shout(\"hello\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "01097ee2",
   "metadata": {},
   "outputs": [],
   "source": [
    "yella = shout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "9d205ebd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.shout(text)>"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yella"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "92cc2fd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO\n"
     ]
    }
   ],
   "source": [
    "print(yella(\"hello\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "7e59aeca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shout(text):\n",
    "    return text.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "3fdf5318",
   "metadata": {},
   "outputs": [],
   "source": [
    "def whisper(text):\n",
    "    return text.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "2d3a9b53",
   "metadata": {},
   "outputs": [],
   "source": [
    "def greet(func):\n",
    "    greeting = func(\"hello , my name is jack i am not terror; \" )\n",
    "    print(greeting)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "0f0a8d0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO , MY NAME IS JACK I AM NOT TERROR; \n"
     ]
    }
   ],
   "source": [
    "greet(shout) # taking as an object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "3e0b3e7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello , my name is jack i am not terror; \n"
     ]
    }
   ],
   "source": [
    "greet(whisper) # taking as an object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "0cdba3c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def crate(x):\n",
    "    def add(y):\n",
    "        return x+y\n",
    "    return add"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "7397c62a",
   "metadata": {},
   "outputs": [],
   "source": [
    "add = crate(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "d7293449",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35\n"
     ]
    }
   ],
   "source": [
    "print(add(20))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e0e3919",
   "metadata": {},
   "source": [
    "# Decorators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "740d38ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function are taken as the arguments into another function and then called inside the wrapper function\n",
    "# @dfg_decorator\n",
    "# def hello_decorator():\n",
    "#     print(\"gfg\")\n",
    "# \"\"\"\n",
    "# above code is equivalent to--\n",
    "# def hello_decorator():\n",
    "# print(\"gfg\")\n",
    "# \"\"\"\n",
    "def decor(func):\n",
    "    def inner():\n",
    "        print(\"inner function : \")\n",
    "        func()\n",
    "    return inner()\n",
    "def function_to():\n",
    "    print(\"this is inside the functin: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "a7747647",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inner function : \n",
      "this is inside the functin: \n"
     ]
    }
   ],
   "source": [
    "to = decor(function_to)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "33f123e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import math\n",
    "def calculate(func):\n",
    "    def inner1(*args,**kwargs):\n",
    "        begin = time.time()\n",
    "        func(*args,**kwargs)\n",
    "        end = time.time()\n",
    "        print(\"total time taken in : \",func.__name__,end-begin)\n",
    "    return inner1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "58c76265",
   "metadata": {},
   "outputs": [],
   "source": [
    "@calculate\n",
    "def factorial(num):\n",
    "    time.sleep(2)\n",
    "    print(math.factorial(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "43ebd843",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n",
      "total time taken in :  factorial 2.007417678833008\n"
     ]
    }
   ],
   "source": [
    "factorial(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "b2d080e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hello_decorat(func):\n",
    "    def inner1(*args,**kwargs):\n",
    "        print(\"before excution :\")\n",
    "        return_value = func(*args,**kwargs)\n",
    "        print(\"after excution: \")\n",
    "        return return_value\n",
    "    return inner1\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "ede95009",
   "metadata": {},
   "outputs": [],
   "source": [
    "@hello_decorat\n",
    "def sm(a,b):\n",
    "    return a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "91ee56b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "before excution :\n",
      "after excution: \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sm(5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "118e0783",
   "metadata": {},
   "outputs": [],
   "source": [
    "def decor1(func):\n",
    "    def inner():\n",
    "        x = func()\n",
    "        return x**2\n",
    "    return inner\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "7f95faf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def decor(func):\n",
    "    def inner():\n",
    "        \n",
    "        x = func()\n",
    "        return x**3\n",
    "    return inner\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "d7593925",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1000000\n"
     ]
    }
   ],
   "source": [
    "@decor1\n",
    "@decor\n",
    "def num():\n",
    "    return 10\n",
    "print(num())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77b94f59",
   "metadata": {},
   "source": [
    "# Decorators with parameters in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "fe73f27d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# @decorator(params):\n",
    "#     def function_name():\n",
    "#         '''function implementation'''\n",
    "def decorators(*args,**kwargs):\n",
    "    def inner(func):\n",
    "        '''\n",
    "        do operation with func\n",
    "        '''\n",
    "        return func\n",
    "    return inner # this is the fun_obj mention in the abouve code\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "1c0e7c96",
   "metadata": {},
   "outputs": [],
   "source": [
    "parms = \"mahesh meti\"\n",
    "@decorators(parms)\n",
    "def func():\n",
    "    \"\"\"\n",
    "    function implementation\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "40bd1ca4",
   "metadata": {},
   "outputs": [],
   "source": [
    "func()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "df56f598",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Decor_fun(func):\n",
    "    print(\"inside decorator: \")\n",
    "    \n",
    "    def inner(*args,**kwargs):\n",
    "        print(\"inside inner function: \")\n",
    "        print(\"decorated the function: \")\n",
    "        func()\n",
    "    return inner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "d636d373",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inside decorator: \n"
     ]
    }
   ],
   "source": [
    "@Decor_fun\n",
    "def func_to():\n",
    "    print(\"inside actuall function: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "12ac6cb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inside inner function: \n",
      "decorated the function: \n",
      "inside actuall function: \n"
     ]
    }
   ],
   "source": [
    "func_to()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "8272f2f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Decorators with parameters in python\n",
    "def Decor_fun(func):\n",
    "    print(\"inside Decorator: \")\n",
    "    def inner(*args,**kwargs):\n",
    "        print(\"inside inner function: \")\n",
    "        print(\"decorated the fucntion: \")\n",
    "        func()\n",
    "    return inner\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "1c86470e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def func_to():\n",
    "    print(\"inside actual function : \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "ef9f7ad4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inside actual function : \n",
      "inside Decorator: \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.Decor_fun.<locals>.inner(*args, **kwargs)>"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Decor_fun(func_to())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "bfcc3ab2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# decorators with parameters in python\n",
    "def decorator (*args, **kwargs):\n",
    "    print(\"inner decorator: \")\n",
    "    def inner(func):\n",
    "        print(\"inside inner function: \")\n",
    "        print(\"i like\",kwargs['like'])\n",
    "        func()\n",
    "    return inner\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "a4cb9fa8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inner decorator: \n",
      "inside inner function: \n",
      "i like manjunath\n",
      "inside actaul function: \n"
     ]
    }
   ],
   "source": [
    "@decorator(like = 'manjunath')\n",
    "def my_func():\n",
    "    print(\"inside actaul function: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "2a55a939",
   "metadata": {},
   "outputs": [],
   "source": [
    "def decorator_func(x,y):\n",
    "    def inner(func):\n",
    "        def wrapper(*args,**kwargs):\n",
    "            print(\"i like geeksforgeeks\")\n",
    "            print(\"summation of values-{}\".format(x+y))\n",
    "            func(*args,**kwargs)\n",
    "        return wrapper\n",
    "    return inner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "bdd1fece",
   "metadata": {},
   "outputs": [],
   "source": [
    "def my_fun(*args):\n",
    "    for ele in args:\n",
    "        print(ele)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "19cf2192",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i like geeksforgeeks\n",
      "summation of values-40\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'NoneType' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/1746111173.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdecorator_func\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m15\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m25\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmy_func\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'geeks'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'for'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'geeks'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/3508206498.py\u001b[0m in \u001b[0;36mwrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m      4\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"i like geeksforgeeks\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"summation of values-{}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m             \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0minner\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'NoneType' object is not callable"
     ]
    }
   ],
   "source": [
    "decorator_func(15,25)(my_func)('geeks','for','geeks')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "d7833fe8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def factor(num):\n",
    "    if num == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return num*(factor(num-1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "c69a5028",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "factor(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "bfb4dc23",
   "metadata": {},
   "outputs": [],
   "source": [
    "def memory(f):\n",
    "    memory1 = {}\n",
    "    def inner(num):\n",
    "        if num not in memory1:\n",
    "            memory1[num]=f(num)\n",
    "        return memory1[num]\n",
    "    return inner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "b081da25",
   "metadata": {},
   "outputs": [],
   "source": [
    "@memory\n",
    "def facto(num):\n",
    "    if num == 1:\n",
    "        return 1\n",
    "    return num * facto(num-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "b4318228",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "facto(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ebf3330",
   "metadata": {},
   "source": [
    "# help function in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "f5ae7539",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Help on NoneType object:\n",
      "\n",
      "class NoneType(object)\n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __bool__(self, /)\n",
      " |      self != 0\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from builtins.type\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# the help function is used to display the documentationn of module ,function classes keywords etc\n",
    "# syntax help([object])\n",
    "help(print())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "69d23bca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on list object:\n",
      "\n",
      "class list(object)\n",
      " |  list(iterable=(), /)\n",
      " |  \n",
      " |  Built-in mutable sequence.\n",
      " |  \n",
      " |  If no argument is given, the constructor creates a new empty list.\n",
      " |  The argument must be an iterable if specified.\n",
      " |  \n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __add__(self, value, /)\n",
      " |      Return self+value.\n",
      " |  \n",
      " |  __contains__(self, key, /)\n",
      " |      Return key in self.\n",
      " |  \n",
      " |  __delitem__(self, key, /)\n",
      " |      Delete self[key].\n",
      " |  \n",
      " |  __eq__(self, value, /)\n",
      " |      Return self==value.\n",
      " |  \n",
      " |  __ge__(self, value, /)\n",
      " |      Return self>=value.\n",
      " |  \n",
      " |  __getattribute__(self, name, /)\n",
      " |      Return getattr(self, name).\n",
      " |  \n",
      " |  __getitem__(...)\n",
      " |      x.__getitem__(y) <==> x[y]\n",
      " |  \n",
      " |  __gt__(self, value, /)\n",
      " |      Return self>value.\n",
      " |  \n",
      " |  __iadd__(self, value, /)\n",
      " |      Implement self+=value.\n",
      " |  \n",
      " |  __imul__(self, value, /)\n",
      " |      Implement self*=value.\n",
      " |  \n",
      " |  __init__(self, /, *args, **kwargs)\n",
      " |      Initialize self.  See help(type(self)) for accurate signature.\n",
      " |  \n",
      " |  __iter__(self, /)\n",
      " |      Implement iter(self).\n",
      " |  \n",
      " |  __le__(self, value, /)\n",
      " |      Return self<=value.\n",
      " |  \n",
      " |  __len__(self, /)\n",
      " |      Return len(self).\n",
      " |  \n",
      " |  __lt__(self, value, /)\n",
      " |      Return self<value.\n",
      " |  \n",
      " |  __mul__(self, value, /)\n",
      " |      Return self*value.\n",
      " |  \n",
      " |  __ne__(self, value, /)\n",
      " |      Return self!=value.\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  __reversed__(self, /)\n",
      " |      Return a reverse iterator over the list.\n",
      " |  \n",
      " |  __rmul__(self, value, /)\n",
      " |      Return value*self.\n",
      " |  \n",
      " |  __setitem__(self, key, value, /)\n",
      " |      Set self[key] to value.\n",
      " |  \n",
      " |  __sizeof__(self, /)\n",
      " |      Return the size of the list in memory, in bytes.\n",
      " |  \n",
      " |  append(self, object, /)\n",
      " |      Append object to the end of the list.\n",
      " |  \n",
      " |  clear(self, /)\n",
      " |      Remove all items from list.\n",
      " |  \n",
      " |  copy(self, /)\n",
      " |      Return a shallow copy of the list.\n",
      " |  \n",
      " |  count(self, value, /)\n",
      " |      Return number of occurrences of value.\n",
      " |  \n",
      " |  extend(self, iterable, /)\n",
      " |      Extend list by appending elements from the iterable.\n",
      " |  \n",
      " |  index(self, value, start=0, stop=9223372036854775807, /)\n",
      " |      Return first index of value.\n",
      " |      \n",
      " |      Raises ValueError if the value is not present.\n",
      " |  \n",
      " |  insert(self, index, object, /)\n",
      " |      Insert object before index.\n",
      " |  \n",
      " |  pop(self, index=-1, /)\n",
      " |      Remove and return item at index (default last).\n",
      " |      \n",
      " |      Raises IndexError if list is empty or index is out of range.\n",
      " |  \n",
      " |  remove(self, value, /)\n",
      " |      Remove first occurrence of value.\n",
      " |      \n",
      " |      Raises ValueError if the value is not present.\n",
      " |  \n",
      " |  reverse(self, /)\n",
      " |      Reverse *IN PLACE*.\n",
      " |  \n",
      " |  sort(self, /, *, key=None, reverse=False)\n",
      " |      Sort the list in ascending order and return None.\n",
      " |      \n",
      " |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the\n",
      " |      order of two equal elements is maintained).\n",
      " |      \n",
      " |      If a key function is given, apply it once to each list item and sort them,\n",
      " |      ascending or descending, according to their function values.\n",
      " |      \n",
      " |      The reverse flag can be set to sort in descending order.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Class methods defined here:\n",
      " |  \n",
      " |  __class_getitem__(...) from builtins.type\n",
      " |      See PEP 585\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from builtins.type\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Data and other attributes defined here:\n",
      " |  \n",
      " |  __hash__ = None\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(dir())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "f645de14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function len in module builtins:\n",
      "\n",
      "len(obj, /)\n",
      "    Return the number of items in a container.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "efd5bc2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function max in module builtins:\n",
      "\n",
      "max(...)\n",
      "    max(iterable, *[, default=obj, key=func]) -> value\n",
      "    max(arg1, arg2, *args, *[, key=func]) -> value\n",
      "    \n",
      "    With a single iterable argument, return its biggest item. The\n",
      "    default keyword-only argument specifies an object to return if\n",
      "    the provided iterable is empty.\n",
      "    With two or more arguments, return the largest argument.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "767dc234",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Helper:\n",
    "    def __init__(self):\n",
    "        \"\"\"the helper class is initialized\"\"\"\n",
    "    def print_help(self):\n",
    "        \"\"\"return the help description\"\"\"\n",
    "        print(\"helper description:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "fbf608b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on class Helper in module __main__:\n",
      "\n",
      "class Helper(builtins.object)\n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __init__(self)\n",
      " |      the helper class is initialized\n",
      " |  \n",
      " |  print_help(self)\n",
      " |      return the help description\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Data descriptors defined here:\n",
      " |  \n",
      " |  __dict__\n",
      " |      dictionary for instance variables (if defined)\n",
      " |  \n",
      " |  __weakref__\n",
      " |      list of weak references to the object (if defined)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(Helper)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "8729ab5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function print_help in module __main__:\n",
      "\n",
      "print_help(self)\n",
      "    return the help description\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(Helper.print_help)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "379f16f4",
   "metadata": {},
   "source": [
    "# python | range deos not return an iterator  function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "bfa5a427",
   "metadata": {},
   "outputs": [],
   "source": [
    "demo = range(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "41ebe23e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 6)"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "demo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "bacbfbb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "range(0, 6)\n"
     ]
    }
   ],
   "source": [
    "print(demo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "c511dc01",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'range' object is not an iterator",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/2933516256.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mnext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdemo\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'range' object is not an iterator"
     ]
    }
   ],
   "source": [
    "next(demo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "460ebd88",
   "metadata": {},
   "outputs": [],
   "source": [
    "demo = iter(range(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "e2a5652c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<range_iterator at 0x2348cb758d0>"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "demo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "021c98ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(demo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "6ac7183e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for i in demo:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "389e637f",
   "metadata": {},
   "outputs": [],
   "source": [
    "demo = iter(range(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "id": "12a8e89c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "data = next(demo)\n",
    "i = 0\n",
    "while (i < data):\n",
    "    print(i)\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "af7d7a02",
   "metadata": {},
   "outputs": [],
   "source": [
    "dt = next(demo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "id": "1612a6cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 204,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "id": "7217df1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "while (dt < 5):\n",
    "    print(dt)\n",
    "    dt+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "id": "1efd9de9",
   "metadata": {},
   "outputs": [],
   "source": [
    "dempo = range(1,32,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "id": "91701b97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(1, 32, 2)"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dempo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "8e323ba2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dempo.start"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "id": "09a890d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 209,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dempo.step"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "ce17887c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dempo.index(23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "1d97f721",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "30 is not in range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/340366733.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdempo\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m30\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: 30 is not in range"
     ]
    }
   ],
   "source": [
    "dempo.index(30)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8987d212",
   "metadata": {},
   "source": [
    "# python bit function on int (bit_length, to_bytes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "9757834d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# we are familiar with function which is also known as a subroutine\n",
    "num = 7\n",
    "print(num.bit_length())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "id": "dc6d49a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "num = -7\n",
    "print(num.bit_length())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f18242e4",
   "metadata": {},
   "source": [
    "# Object_Oriented concept\n",
    "## python intermediate level topics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "id": "1c5b97f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creates a class named myclass\n",
    "class MyClass:\n",
    "    number = '0'\n",
    "    name = \"manjunath kannur\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "id": "855c05df",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    me = MyClass()\n",
    "    me.number = '1030'\n",
    "    me.name = \"harsha\"\n",
    "    print(me.name)\n",
    "    print(me.name + \" \"+ str(me.number))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "b1be590a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "harsha\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'int' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/2949861635.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/2968472406.py\u001b[0m in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mme\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"harsha\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mme\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mme\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m\" \"\u001b[0m\u001b[1;33m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mme\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnumber\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not callable"
     ]
    }
   ],
   "source": [
    "if __name__=='__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "c0783d8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Methods \n",
    "# function that belongs to class is called mehtod\n",
    "class Vector:\n",
    "    x = 0.0\n",
    "    y = 0.0\n",
    "    def set(self,x,y):\n",
    "        self.x = x \n",
    "        self.y = y\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "360e7a29",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Main():\n",
    "    vec = Vector()\n",
    "    vec.set(5,6)\n",
    "#     print(\"X :\" + str(vec.x)+ \", Y:\"+str(vec.y))\n",
    "    print(vec.x)\n",
    "    print(vec.y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "d0355893",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "if __name__=='__main__':\n",
    "    Main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74ac908c",
   "metadata": {},
   "source": [
    "# Inheritance \n",
    "## inheritance is defined as a way in which a particular class\n",
    "# syntax for inheritance \n",
    "## class derived-classname(superclass_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "508e574f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# base class \n",
    "# superclass\n",
    "class Pet:\n",
    "    # __init__ is an constructor in python\n",
    "    def __init__(self,name,age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "class Cat(Pet):\n",
    "    def __init__(self,name , age):\n",
    "        super().__init__(name , age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "ef13dee4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Main():\n",
    "    thepet = Pet('cat',1)\n",
    "    jess = Cat('pet',2)\n",
    "    # isinstance() function to check whether a class is \n",
    "    #inherited from another class\n",
    "#     print(\"is jess a cat?\" +str(isinstance(jess,Cat)))\n",
    "#     print(\"is jess a Pet?\" +str(isinstance(jess,Pet)))\n",
    "#     print(\"is jess a Pet?\" +str(isinstance(thepet,Cat)))\n",
    "#     print(\"is jess a Pet?\" +str(isinstance(thepet,Pet)))\n",
    "    print(jess.name)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "id": "d31a5954",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pet\n"
     ]
    }
   ],
   "source": [
    "if __name__=='__main__':\n",
    "    Main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "id": "2102e48e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# iterators\n",
    "## iterators are object that can be iterated upon\n",
    "class Reverse:\n",
    "    def __init__(self,data):\n",
    "        self.data = data\n",
    "        self.index = len(data)\n",
    "        \n",
    "    def __iter__(self):\n",
    "        return self\n",
    "    def __next__(self):\n",
    "        if self.index == 0:\n",
    "            raise  StopIteration\n",
    "        self.index -= 1\n",
    "        return self.data[self.index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "id": "480bd427",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    rev = Reverse('Drapsicle')\n",
    "    for char in rev:\n",
    "        print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "id": "bcf81ec0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e\n",
      "l\n",
      "c\n",
      "i\n",
      "s\n",
      "p\n",
      "a\n",
      "r\n",
      "D\n"
     ]
    }
   ],
   "source": [
    "if __name__=='__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "id": "b1f7c065",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Reverse(data):\n",
    "    for index in range(len(data)-1,-1,-1):\n",
    "        yield data[index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "id": "fda7c9cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    rev = Reverse('harsh')\n",
    "    for char in rev:\n",
    "        print(char)\n",
    "    data = 'harssh'\n",
    "    print(list(data[i] for i in range(len(data)-1,-1,-1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "id": "b938efd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "h\n",
      "s\n",
      "r\n",
      "a\n",
      "h\n",
      "['h', 's', 's', 'r', 'a', 'h']\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af521728",
   "metadata": {},
   "source": [
    "# Main Concepts of object- oriented programming(oops)\n",
    "1. class\n",
    "2. objects\n",
    "3. polymorphism\n",
    "4. encapsulation\n",
    "5. inheritance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05f8846f",
   "metadata": {},
   "source": [
    "# class A class is a collection of objects. A class contains the blueprints\n",
    "1. class are created by keyword class\n",
    "2. attirbutes are the variables that belong to a class\n",
    "3. attributes are always public and can be accessed using the dot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "id": "5ba72570",
   "metadata": {},
   "outputs": [],
   "source": [
    "# class classname:\n",
    "#     # statement-1\n",
    "#     # statement- n\n",
    "class  Dog:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "18f4eb0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "var = Dog()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "id": "8209daf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.Dog object at 0x000002348CBB2DC0>\n"
     ]
    }
   ],
   "source": [
    "print(var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "id": "80fb8731",
   "metadata": {},
   "outputs": [],
   "source": [
    "# objects the object is an entity that has a state and behavior associated with it\n",
    "# state : it is represented by the attributes of an object. it also reflects the properties of an object\n",
    "obj = Dog()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "id": "71ed5f9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Dog at 0x2348cbb2190>"
      ]
     },
     "execution_count": 263,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e53cb8d5",
   "metadata": {},
   "source": [
    "# creating a class and object with class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "id": "ff764b12",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Dog:\n",
    "    attr = \"kannur\"\n",
    "    def __init__(self,name):\n",
    "        self.name = name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "id": "719d4a6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "rodger = Dog(\"manjunath\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "id": "6e33088b",
   "metadata": {},
   "outputs": [],
   "source": [
    "tommy = Dog(\"tommy\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "id": "5e0e11cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Dog at 0x2348cbb2580>"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tommy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "id": "8bdc4087",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rodger is a kannur\n",
      "tommy is also a kannur\n"
     ]
    }
   ],
   "source": [
    "print(\"rodger is a {}\".format(rodger.__class__.attr))\n",
    "print('tommy is also a {}'.format(tommy.__class__.attr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "id": "ec3e419c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is manjunath\n",
      "my name is tommy\n"
     ]
    }
   ],
   "source": [
    "print(\"my name is {}\".format(rodger.name))\n",
    "print(\"my name is {}\".format(tommy.name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "id": "b7c0b043",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Dog:\n",
    "    attr = \"kannur\"\n",
    "    def __init__(self,name):\n",
    "        self.name = name\n",
    "        \n",
    "    def speak(self):\n",
    "        print(\"my name is {}\".format(self.name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "28c3a69b",
   "metadata": {},
   "outputs": [],
   "source": [
    "rodger = Dog(\"roader\")\n",
    "tommy = Dog('tommy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "id": "59f52540",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is roader\n"
     ]
    }
   ],
   "source": [
    "rodger.speak()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "id": "04507a74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is tommy\n"
     ]
    }
   ],
   "source": [
    "tommy.speak()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a8e3e00",
   "metadata": {},
   "source": [
    "# inheritance\n",
    "## inheritance is the capability of one class to derive "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "id": "b4803ec2",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person(object):\n",
    "    # __init__ is known as the constructor\n",
    "    def __init__(self,name,idnumber):\n",
    "        self.name = name\n",
    "        self.idnumber = idnumber\n",
    "        \n",
    "    def display(self):\n",
    "        print(self.name)\n",
    "        print(self.idnumber)\n",
    "    def details(self):\n",
    "        print(\"my name is {}\".format(self.name))\n",
    "        print(\"idnumber is {}\".format(self.idnumber))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "id": "480a3c15",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Emp(Person):\n",
    "    def __init__(self,name,idnumber,salary,post):\n",
    "        self.salary = salary\n",
    "        self.post = post\n",
    "        Person.__init__(self,name,idnumber)\n",
    "    def details(self):\n",
    "        print(\"my name is {}\".format(self.name))\n",
    "        print(\"idnumber : {}\".format(self.idnumber))\n",
    "        print(\"post : {}\".format(self.post))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "id": "f8c32028",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = Emp('rahul',25,20,'intern')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "id": "0c675faf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Emp at 0x2348cb8fa90>"
      ]
     },
     "execution_count": 279,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "id": "7b90e8c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rahul\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "a.display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "4d440e68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is rahul\n",
      "idnumber : 25\n",
      "post : intern\n"
     ]
    }
   ],
   "source": [
    "a.details()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 294,
   "id": "b12a30ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "class kannur:\n",
    "    def __init__(self,name,age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "    def details(self):\n",
    "        print(self.name)\n",
    "        print(self.age)\n",
    "    def display(self):\n",
    "        print(\"the name is {}\".format(self.name))\n",
    "        print(\"the age is {}\".format(self.age))\n",
    "        \n",
    "class manjunath(kannur):\n",
    "    def __init__(self,name,age,salary,post):\n",
    "        self.salary = salary\n",
    "        self.post = post\n",
    "        kannur.__init__(self,name,age)\n",
    "    def details(self):\n",
    "        print(\"my name is {}\".format(self.name))\n",
    "        print(\"my age is {}\".format(self.age))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 295,
   "id": "5dff6058",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = manjunath('manjunath',55,68,'kannur')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
   "id": "9c908eae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is manjunath\n",
      "my age is 55\n"
     ]
    }
   ],
   "source": [
    "a.details()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 297,
   "id": "5a47f9a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bird:\n",
    "    def intro(self):\n",
    "        print(\"there are many types of birds: \")\n",
    "    def flight(self):\n",
    "        print(\"most of the birds can fly but some connot: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 298,
   "id": "96b21e97",
   "metadata": {},
   "outputs": [],
   "source": [
    "class sparrow(Bird):\n",
    "    def flight(self):\n",
    "        print(\"sparrows can fly.\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 299,
   "id": "56bf4cc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "class ostrich(Bird):\n",
    "    def flight(self):\n",
    "        print(\"ostriches cannot fly.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "id": "a3784d54",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj_bird = Bird()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 301,
   "id": "877c0821",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Bird at 0x2348cbd2760>"
      ]
     },
     "execution_count": 301,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj_bird"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 302,
   "id": "a77affee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "there are many types of birds: \n"
     ]
    }
   ],
   "source": [
    "obj_bird.intro()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 303,
   "id": "f32ccebe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "most of the birds can fly but some connot: \n"
     ]
    }
   ],
   "source": [
    "obj_bird.flight()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "id": "680fd479",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj_ost = ostrich()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "id": "66488358",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ostriches cannot fly.\n"
     ]
    }
   ],
   "source": [
    "obj_ost.flight()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "id": "8ca3ce4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "there are many types of birds: \n"
     ]
    }
   ],
   "source": [
    "obj_ost.intro()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 307,
   "id": "f4d0d933",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj_spr = sparrow()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 308,
   "id": "3ad994fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sparrows can fly.\n"
     ]
    }
   ],
   "source": [
    "obj_spr.flight()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 309,
   "id": "b4c69a14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "there are many types of birds: \n"
     ]
    }
   ],
   "source": [
    "obj_spr.intro()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 310,
   "id": "616cc8ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Base:\n",
    "    def __init__(self):\n",
    "        self.a= 'geeksforgeeks'\n",
    "        self.__c = 'geeksforgeeks'\n",
    "class Derive(Base):\n",
    "    def __init__(self): # constructor \n",
    "        Base.__init__(self)\n",
    "        print(\"calling pirvate memeber of base class: \")\n",
    "        print(self.__c)\n",
    "            \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "id": "a123adb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj1= Base()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "id": "d17beb48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'geeksforgeeks'"
      ]
     },
     "execution_count": 312,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj1.a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "id": "dbd52cde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "calling pirvate memeber of base class: \n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'Derive' object has no attribute '_Derive__c'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/26921422.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mobj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mDerive\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10668/953773592.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m      7\u001b[0m         \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"calling pirvate memeber of base class: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__c\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'Derive' object has no attribute '_Derive__c'"
     ]
    }
   ],
   "source": [
    "obj = Derive()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e86e870a",
   "metadata": {},
   "source": [
    "# python oops Concept\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "id": "12f162f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# python object- oriented programming(oops) is a programming that uses objects and classes\n",
    "# class Classname :\n",
    "#     statement-1\n",
    "#     statement - n\n",
    "class Demo:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "id": "f328b9f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj = Demo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "id": "4cd2c3d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Demo at 0x2348cb8f6d0>"
      ]
     },
     "execution_count": 318,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "id": "15815d2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Demo:\n",
    "    attr = \"manjunath\"\n",
    "    def __init__(self,name):\n",
    "        self.name = name\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "id": "ed3a8d6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "rodger = Demo('renukadevi')\n",
    "tommy = Demo(\"tommy\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "id": "805ef080",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Demo at 0x2348cb816a0>"
      ]
     },
     "execution_count": 321,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tommy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 323,
   "id": "fd0548e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'tommy'"
      ]
     },
     "execution_count": 323,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tommy.name"
   ]
  },
  {
   "cell_type": "raw",
   "id": "e94c5e2a",
   "metadata": {},
   "source": [
    "rodger.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "id": "4b78ec24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Demo at 0x2348cb81490>"
      ]
     },
     "execution_count": 324,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rodger"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "id": "bf896084",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'renukadevi'"
      ]
     },
     "execution_count": 325,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rodger.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 327,
   "id": "9fec6dec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rodger is a manjunath\n"
     ]
    }
   ],
   "source": [
    "print(\"rodger is a {}\".format(rodger.__class__.attr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "id": "a7eef076",
   "metadata": {},
   "outputs": [],
   "source": [
    "class kannur:\n",
    "    # class attribute\n",
    "    attr = \"kannur\"\n",
    "    # instance attribute\n",
    "    def __init__(self,name):\n",
    "        self.name = name\n",
    "rodger = kannur('manjunath')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
   "id": "8b130a39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is manjunath\n",
      "my name is kannur\n"
     ]
    }
   ],
   "source": [
    "print(\"my name is {}\".format(rodger.name)) # instance attribute\n",
    "print(\"my name is {}\".format(rodger.__class__.attr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "id": "06a1964d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is tommy\n",
      "my name is manjunath\n"
     ]
    }
   ],
   "source": [
    "print(\"my name is {}\".format(tommy.name))\n",
    "print(\"my name is {}\".format(tommy.__class__.attr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 334,
   "id": "02b0c214",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is tommy\n",
      "my name is manjunath\n"
     ]
    }
   ],
   "source": [
    "print(\"my name is {}\".format(tommy.name))\n",
    "print(\"my name is {}\".format(tommy.__class__.attr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "id": "b05d4c4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Dog :\n",
    "    attr = \"mammal\"\n",
    "    def __init__(self,name):\n",
    "        self.name = name\n",
    "    def speak(self):\n",
    "        print(\"my name is {}\".format(self.name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 336,
   "id": "3ad9d9ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "rodger = Dog('rodger')\n",
    "tommy = Dog('tommy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 337,
   "id": "c724396a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is rodger\n"
     ]
    }
   ],
   "source": [
    "rodger.name # instance attributes\n",
    "rodger.__class__.attr # class attributes\n",
    "rodger.speak() # accessing class method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 338,
   "id": "23ed26ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is tommy\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'mammal'"
      ]
     },
     "execution_count": 338,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tommy.speak()\n",
    "tommy.name\n",
    "tommy.__class__.attr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 339,
   "id": "1c9786f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'mammal'"
      ]
     },
     "execution_count": 339,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rodger.__class__.attr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4193d4e4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
