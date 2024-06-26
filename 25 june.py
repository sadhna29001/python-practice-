{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to NumPy\n",
    "* NumPy (Numerical Python) is a fundamental library for numerical operations in Python. It provides efficient support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays.\n",
    "## Benefits of using NumPy over standard Python lists:\n",
    "* NumPy arrays are more compact in memory and faster in execution.\n",
    "* NumPy provides a wide range of mathematical functions and operations optimized for scientific computing.\n",
    "* NumPy arrays can be easily integrated with other scientific computing libraries like SciPy and Matplotlib."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Installing NumPy\n",
    "* You can install NumPy using the Python package installer pip:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting numpy\n",
      "  Downloading numpy-1.26.4-cp39-cp39-macosx_11_0_arm64.whl (14.0 MB)\n",
      "\u001b[K     |████████████████████████████████| 14.0 MB 145 kB/s eta 0:00:01    |█▋                              | 716 kB 147 kB/s eta 0:01:31\n",
      "\u001b[?25hInstalling collected packages: numpy\n",
      "Successfully installed numpy-1.26.4\n",
      "\u001b[33mWARNING: You are using pip version 21.2.4; however, version 24.0 is available.\n",
      "You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* To verify the installation and check the NumPy version, you can use:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.26.4\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "print(np.__version__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NumPy Arrays\n",
    "* NumPy arrays are the core data structure in NumPy. They are similar to Python lists but more efficient and optimized for numerical operations."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Some commonly used numpy Attributes: \n",
    "1. shape: The shape attribute returns a tuple representing the dimensions of the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5,)\n",
      "(2, 3)\n",
      "(2, 2, 2)\n"
     ]
    }
   ],
   "source": [
    "# 1D array\n",
    "a = np.array([1, 2, 3, 4, 5])\n",
    "print(a.shape)  \n",
    "\n",
    "# 2D array\n",
    "b = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "print(b.shape)  \n",
    "\n",
    "# 3D array\n",
    "c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])\n",
    "print(c.shape)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. size: The size attribute returns the total number of elements in the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "print(a.size) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. dtype: The dtype attribute represents the data type of the array elements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int64\n",
      "float64\n",
      "complex128\n",
      "bool\n"
     ]
    }
   ],
   "source": [
    "# Integer array\n",
    "a = np.array([1, 2, 3, 4, 5])\n",
    "print(a.dtype) \n",
    "\n",
    "# Float array\n",
    "b = np.array([1.0, 2.0, 3.0])\n",
    "print(b.dtype)  \n",
    "\n",
    "# Complex array\n",
    "c = np.array([1+2j, 3+4j])\n",
    "print(c.dtype)  \n",
    "\n",
    "# Boolean array\n",
    "d = np.array([True, False, True])\n",
    "print(d.dtype)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* You can also specify the data type when creating an array using the dtype parameter:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 2. 3.]\n",
      "float32\n"
     ]
    }
   ],
   "source": [
    "# Create an array with float32 data type\n",
    "a = np.array([1, 2, 3], dtype=np.float32)\n",
    "print(a)        \n",
    "print(a.dtype)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n",
      "int16\n"
     ]
    }
   ],
   "source": [
    "# Create an array with int16 data type\n",
    "b = np.array([1, 2, 3], dtype=np.int16)\n",
    "print(b)        \n",
    "print(b.dtype)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Some commonly used functions to create arrays:\n",
    "1. np.array(): Create an array from a Python list or sequence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "# From a list\n",
    "a = np.array([1, 2, 3, 4, 5])\n",
    "print(a)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10 20 30]\n"
     ]
    }
   ],
   "source": [
    "# From a sequence\n",
    "b = np.array((10, 20, 30))\n",
    "print(b)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. np.asarray(): Convert the input to an array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n",
      "[10 20 30]\n"
     ]
    }
   ],
   "source": [
    "# From a list\n",
    "c = [1, 2, 3, 4, 5]\n",
    "a = np.asarray(c)\n",
    "print(a)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10 20 30]\n"
     ]
    }
   ],
   "source": [
    "# From a tuple\n",
    "d = (10, 20, 30)\n",
    "b = np.asarray(d)\n",
    "print(b)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. np.ones(): Create an array filled with ones."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "# Create a 1D array of ones\n",
    "a = np.ones(5)\n",
    "print(a)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 1. 1.]\n",
      " [1. 1. 1. 1.]\n",
      " [1. 1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# Create a 2D array of ones with shape (3, 4)\n",
    "b = np.ones((3, 4))\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. np.zeros(): Create an array filled with zeros."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "# Create a 1D array of zeros\n",
    "a = np.zeros(5)\n",
    "print(a)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0.]\n",
      " [0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "# Create a 2D array of zeros with shape (2, 3)\n",
    "b = np.zeros((2, 3))\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. np.empty(): Create an uninitialized array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "# Create an uninitialized 1D array\n",
    "a = np.empty(5)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0.]\n",
      " [0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "# Create an uninitialized 2D array with shape (2, 3)\n",
    "b = np.empty((2, 3))\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. np.arange(): Create a sequence of numbers within a range."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "# Create a sequence from 0 to 9\n",
    "a = np.arange(10)\n",
    "print(a)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  4  6  8 10]\n"
     ]
    }
   ],
   "source": [
    "# Create a sequence from 2 to 10 with step size 2\n",
    "b = np.arange(2, 11, 2)\n",
    "print(b)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. np.linspace(): Create an array with evenly spaced values within a range."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.   0.25 0.5  0.75 1.  ]\n"
     ]
    }
   ],
   "source": [
    "# Create an array with 5 evenly spaced values between 0 and 1\n",
    "a = np.linspace(0, 1, 5)\n",
    "print(a) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0.    1.25  2.5   3.75  5.    6.25  7.5   8.75 10.  ]\n"
     ]
    }
   ],
   "source": [
    "# Create an array with 9 evenly spaced values between 0 and 10\n",
    "b = np.linspace(0, 10, 9)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. np.eye(): Create a square identity matrix."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0.]\n",
      " [0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# Create a 2x2 identity matrix\n",
    "a = np.eye(2)\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# Create a 3x3 identity matrix\n",
    "a = np.eye(3)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numpy Array Operations and Broadcasting"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Basic Array Operations**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Addition: Adds two arrays element-wise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 7 9]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "b = np.array([4, 5, 6])\n",
    "\n",
    "c = a + b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Subtraction: Subtracts two arrays element-wise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 3 3]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "b = np.array([4, 5, 6])\n",
    "\n",
    "c = b - a\n",
    "print(c) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Multiplication: Multiplies two arrays element-wise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 4 10 18]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "b = np.array([4, 5, 6])\n",
    "\n",
    "c = a * b\n",
    "print(c)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Division: Divides two arrays element-wise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4.  2.5 2. ]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "b = np.array([4, 5, 6])\n",
    "\n",
    "c = b / a\n",
    "print(c)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Scalar Operations: Multiplies/Divides each element of the array by the scalar value; \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 6]\n",
      "[0.5 1.  1.5]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "\n",
    "b = a * 2\n",
    "print(b)  \n",
    "\n",
    "c = a / 2\n",
    "print(c) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Square Root(np.sqrt()): Computes the square root of each element in the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 2. 3.]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 4, 9])\n",
    "\n",
    "b = np.sqrt(a)\n",
    "print(b) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Exponential(np.exp()): Computes the exponential of each element in the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2.71828183  7.3890561  20.08553692]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "\n",
    "b = np.exp(a)\n",
    "print(b) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Broadcasting**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Broadcasting is a powerful mechanism in NumPy that allows arithmetic operations between arrays with different shapes. \n",
    "- It automatically duplicates the smaller array along the missing dimensions to match the shape of the larger array. \n",
    "- This makes it possible to perform operations on arrays with different shapes without explicitly reshaping them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1D Array and Scalar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 4 5]\n"
     ]
    }
   ],
   "source": [
    "# 1D array and scalar\n",
    "a = np.array([1, 2, 3])\n",
    "b = 2\n",
    "c = a + b  \n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2D Array and 1D Array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[11 22 33]\n",
      " [14 25 36]]\n"
     ]
    }
   ],
   "source": [
    "# 2D array and 1D array\n",
    "a = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "b = np.array([10, 20, 30])\n",
    "c = a + b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Broadcasting follows certain rules:\n",
    "\n",
    "- If the arrays have the same shape, no broadcasting is necessary, and the operation is performed element-wise.\n",
    "- If the arrays have different shapes, NumPy attempts to broadcast the smaller array's shape to match the larger array's shape.\n",
    "- If the dimensions of the arrays are different, NumPy starts from the trailing dimensions and works backward, prepending 1s to the smaller shape until the shapes match.\n",
    "- If the shapes still don't match after prepending 1s, NumPy raises a ValueError."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Example Of Where Broadcasting is not possible"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "operands could not be broadcast together with shapes (2,3) (3,2) ",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[13], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m a \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([[\u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m, \u001b[38;5;241m3\u001b[39m], [\u001b[38;5;241m4\u001b[39m, \u001b[38;5;241m5\u001b[39m, \u001b[38;5;241m6\u001b[39m]])\n\u001b[0;32m      3\u001b[0m b \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([[\u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m], [\u001b[38;5;241m3\u001b[39m, \u001b[38;5;241m4\u001b[39m], [\u001b[38;5;241m5\u001b[39m, \u001b[38;5;241m6\u001b[39m]])\n\u001b[1;32m----> 4\u001b[0m c \u001b[38;5;241m=\u001b[39m \u001b[43ma\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m  \n",
      "\u001b[1;31mValueError\u001b[0m: operands could not be broadcast together with shapes (2,3) (3,2) "
     ]
    }
   ],
   "source": [
    "# Different shapes: (2, 3) and (3, 2)\n",
    "a = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "b = np.array([[1, 2], [3, 4], [5, 6]])\n",
    "c = a + b  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**3. Element-wise Operations And Their Efficiency**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- In NumPy, element-wise operations are performed on arrays in a highly efficient manner. \n",
    "- This efficiency comes from the fact that NumPy is written in a combination of Python and optimized C code, allowing it to leverage the computational power of low-level languages like C for numerical operations.\n",
    "- Element-wise operations in NumPy are vectorized, meaning that they are applied to entire arrays at once, rather than iterating over individual elements. - This vectorization is a key factor in NumPy's efficiency, as it avoids the overhead of Python-level loops and allows the operations to be performed in a single step."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Here's an example of how element-wise operations are efficient in NumPy:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NumPy element-wise addition took: 0.086844 seconds\n",
      "Python list element-wise addition took: 12.424693 seconds\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "\n",
    "# Create large arrays\n",
    "a = np.random.rand(10000000)\n",
    "b = np.random.rand(10000000)\n",
    "\n",
    "# Element-wise operations in NumPy\n",
    "start = time.time()\n",
    "c = a + b\n",
    "end = time.time()\n",
    "print(f\"NumPy element-wise addition took: {end - start:.6f} seconds\")\n",
    "\n",
    "# Element-wise operations in Python lists\n",
    "start = time.time()\n",
    "x = [i for i in range(10000000)]\n",
    "y = [i for i in range(10000000)]\n",
    "z = [x[i] + y[i] for i in range(10000000)]\n",
    "end = time.time()\n",
    "print(f\"Python list element-wise addition took: {end - start:.6f} seconds\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, the element-wise addition operation in NumPy is significantly faster than the equivalent operation on Python lists, even for large arrays or lists with millions of elements."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This efficiency is achieved through several factors:\n",
    "\n",
    "- Vectorization: NumPy can perform operations on entire arrays in a single step, avoiding the overhead of Python-level loops.\n",
    "- Optimized C code: NumPy's core operations are written in optimized C code, which is much faster than pure Python code.\n",
    "- Contiguous memory layout: NumPy arrays are stored in a contiguous block of memory, which allows for efficient memory access and cache optimization.\n",
    "- Parallelization: Some NumPy operations can take advantage of multi-core processors and parallel computing, further improving performance."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Indexing and Slicing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **1. Indexing**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Indexing in NumPy arrays is a way to access individual elements or subsets of the array data. \n",
    "- NumPy provides various indexing techniques that allow you to work with arrays in a flexible and efficient manner."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**a) Basic Indexing**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- You can access individual elements using their position indices, similar to Python lists.\n",
    "- For 1D arrays, you provide a single index.\n",
    "- For multidimensional arrays, you provide a tuple of indices, one for each dimension."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "# 1D array\n",
    "a = np.array([1, 2, 3, 4, 5])\n",
    "print(a[0])  \n",
    "print(a[3])  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "# 2D array\n",
    "b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "print(b[0, 0])  \n",
    "print(b[2, 1])  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**b) Fancy Indexing**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Fancy indexing allows you to select elements or subarrays using arrays of integers or boolean arrays.\n",
    "- This is useful when you need to select arbitrary elements or subarrays based on specific conditions or indices."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 3 5]\n"
     ]
    }
   ],
   "source": [
    "# 1D array\n",
    "a = np.array([1, 2, 3, 4, 5])\n",
    "indices = np.array([0, 2, 4])\n",
    "print(a[indices])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 9]\n"
     ]
    }
   ],
   "source": [
    "# 2D array\n",
    "b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "rows = np.array([0, 2])\n",
    "cols = np.array([0, 2])\n",
    "print(b[rows, cols])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**c) Boolean Indexing**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Boolean indexing is a powerful way to select elements or subarrays based on a condition or boolean array.\n",
    "- It allows you to filter the array based on specific criteria."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4 5]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "print(a[a > 3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "print(b[b > 5]) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **2. Slicing**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Slicing in NumPy arrays is a powerful technique that allows you to extract a subset or a view of an array based on specified indices or ranges. \n",
    "- NumPy's slicing is similar to Python's list slicing but extends to multidimensional arrays."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**a) One-Dimensional Array Slicing**\n",
    "- You can slice a 1D array using the start:stop:step notation, just like in Python lists.\n",
    "- The start index is inclusive, and the stop index is exclusive."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 4 5 6]\n",
      "[1 2 3 4]\n",
      "[6 7 8 9]\n",
      "[1 3 5 7 9]\n",
      "[9 8 7 6 5 4 3 2 1]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])\n",
    "print(a[2:6])  \n",
    "print(a[:4])   \n",
    "print(a[5:])   \n",
    "print(a[::2])\n",
    "print(a[::-1]) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**b) Multidimensional Array Slicing**\n",
    "- For multidimensional arrays, you can specify a slice for each dimension, separated by commas.\n",
    "- If you omit a dimension in the slicing, it selects all elements along that dimension."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [4 5]]\n",
      "[2 5 8]\n",
      "[[4 5]\n",
      " [7 8]]\n"
     ]
    }
   ],
   "source": [
    "b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "print(b[0:2, 0:2])  \n",
    "print(b[:, 1])      \n",
    "print(b[1:, :2])    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**c) Slicing with Step size**\n",
    "- You can also specify a step size for slicing by providing a third value in the start:stop:step notation.\n",
    "- Negative step sizes are allowed, which reverses the order of the elements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 4 7]\n",
      "[9 7 5 3 1]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])\n",
    "print(a[::3])  \n",
    "print(a[::-2]) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**d) Assigning Values To Slices**\n",
    "- You can assign values to a slice of an array, which modifies the original array.\n",
    "- The assigned value should have a compatible shape with the slice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1 10 10 10  5]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "a[1:4] = 10\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Array Manipulation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. **Reshaping Arrays**\n",
    "- Reshaping is the process of changing the shape (dimensions) of an array without modifying its data. \n",
    "- This is useful when you need to work with the same data in a different dimensional representation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6,)\n",
      "[[1 2 3]\n",
      " [4 5 6]]\n",
      "[[[1 2 3]]\n",
      "\n",
      " [[4 5 6]]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6])\n",
    "print(a.shape)  \n",
    "\n",
    "# Reshape to a 2D array\n",
    "b = a.reshape(2, 3)\n",
    "print(b)\n",
    "\n",
    "# Reshape to a 3D array\n",
    "c = a.reshape(2, 1, 3)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **2. Flattening Arrays**\n",
    "- Flattening is the process of converting a multidimensional array into a one-dimensional (1D) array. \n",
    "- This can be useful when you need to operate on all elements of the array as a single sequence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n",
      "[1 2 3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "print(a.shape)  \n",
    "\n",
    "# Flatten the array\n",
    "b = a.ravel()\n",
    "print(b)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **3. Concatenating Arrays**\n",
    "- Concatenation is the process of joining two or more arrays together, either along a new axis (stacking) or along an existing axis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n",
      "[1 2 3 4 5 6]\n",
      "[[1 2]\n",
      " [3 4]\n",
      " [5 6]\n",
      " [7 8]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "b = np.array([4, 5, 6])\n",
    "\n",
    "# Concatenate along a new axis (stacking)\n",
    "c = np.stack((a, b))\n",
    "print(c)\n",
    "\n",
    "# Concatenate along an existing axis (horizontal)\n",
    "d = np.concatenate((a, b), axis=None)\n",
    "print(d)  \n",
    "\n",
    "# Concatenate along an existing axis (vertical)\n",
    "e = np.array([[1, 2], [3, 4]])\n",
    "f = np.array([[5, 6], [7, 8]])\n",
    "g = np.concatenate((e, f), axis=0)\n",
    "print(g)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Stacking and Splitting of Arrays\n",
    "In NumPy, stacking and splitting are operations that allow you to combine or divide arrays along different axes. These operations are particularly useful when working with multidimensional arrays and can help you organize and manipulate data more effectively."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **1. Stacking Arrays**\n",
    "Stacking is the process of combining arrays along a new axis. NumPy provides several functions for stacking arrays:\n",
    "\n",
    "- np.stack(arrays, axis=0): <br>\n",
    "This function stacks the arrays along a new axis. The axis parameter specifies the axis along which the arrays are stacked.\n",
    "- np.vstack(arrays): <br>\n",
    "This function stacks the arrays vertically (row-wise) by combining them along the first axis (axis=0).\n",
    "- np.hstack(arrays): <br>\n",
    "This function stacks the arrays horizontally (column-wise) by combining them along the second axis (axis=1)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n",
      "[[1 2]\n",
      " [3 4]]\n",
      "[[1 3]\n",
      " [2 4]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2])\n",
    "b = np.array([3, 4])\n",
    "\n",
    "# Stack arrays horizontally\n",
    "c = np.hstack((a, b))\n",
    "print(c)\n",
    "\n",
    "# Stack arrays vertically\n",
    "d = np.vstack((a, b))\n",
    "print(d)\n",
    "\n",
    "# Stack arrays along a new axis\n",
    "e = np.stack((a, b), axis=1)\n",
    "print(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **2. Splitting Arrays**\n",
    "Splitting is the opposite operation of stacking, where an array is divided into multiple sub-arrays along a specified axis. <br>\n",
    "<br>\n",
    "NumPy provides several functions for splitting arrays:\n",
    "\n",
    "\n",
    "- np.split(array, indices_or_sections, axis=0): <br>\n",
    "This function splits the array into multiple sub-arrays along the specified axis. You can either provide the indices where the array should be split or the number of equal sections to split the array into.\n",
    "- np.vsplit(array, indices_or_sections): <br>\n",
    "This function splits the array vertically (row-wise) by dividing it along the first axis (axis=0).\n",
    "- np.hsplit(array, indices_or_sections): <br>\n",
    "This function splits the array horizontally (column-wise) by dividing it along the second axis (axis=1)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Horizontal split:\n",
      "Left sub-array:\n",
      " [[ 1  2]\n",
      " [ 5  6]\n",
      " [ 9 10]\n",
      " [13 14]]\n",
      "Right sub-array:\n",
      " [[ 3  4]\n",
      " [ 7  8]\n",
      " [11 12]\n",
      " [15 16]]\n"
     ]
    }
   ],
   "source": [
    "# Create a 2D array\n",
    "a = np.array([[1, 2, 3, 4],\n",
    "              [5, 6, 7, 8],\n",
    "              [9, 10, 11, 12],\n",
    "              [13, 14, 15, 16]])\n",
    "\n",
    "# Split the array horizontally into 2 sub-arrays\n",
    "left, right = np.hsplit(a, 2)\n",
    "print(\"Horizontal split:\")\n",
    "print(\"Left sub-array:\\n\", left)\n",
    "print(\"Right sub-array:\\n\", right)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Methods for Adding and Removing elements\n",
    "NumPy provides several methods for adding and removing elements from arrays. These operations are particularly useful when you need to modify the size or shape of an array dynamically. <br>\n",
    "Here are some common methods for adding and removing elements:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **1. Appending Elements**\n",
    "##### np.append(arr, values, axis=None):\n",
    "- This method appends the values to the end of the arr array. <br>\n",
    "- The axis parameter specifies the axis along which the values are appended. <br>\n",
    "- If axis is not provided, it flattens the input array and appends the values as a flat sequence.\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n",
      "[[1 2]\n",
      " [3 4]\n",
      " [5 6]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3])\n",
    "b = np.append(a, [4, 5])\n",
    "print(b)  \n",
    "\n",
    "c = np.array([[1, 2], [3, 4]])\n",
    "d = np.append(c, [[5, 6]], axis=0)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **2. Inserting Elements**\n",
    "##### np.insert(arr, obj, values, axis=None):\n",
    "- This method inserts the values into the arr array before the elements at the specified obj indices. \n",
    "- The axis parameter specifies the axis along which the values are inserted."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2 10 20  3  4  5]\n",
      "[[ 1 10  2]\n",
      " [ 3 20  4]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "b = np.insert(a, 2, [10, 20])\n",
    "print(b) \n",
    "\n",
    "c = np.array([[1, 2], [3, 4]])\n",
    "d = np.insert(c, 1, [10, 20], axis=1)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **3. Deleting Elements**\n",
    "##### np.delete(arr, obj, axis=None): \n",
    "- This method removes the elements from the arr array at the specified obj indices. \n",
    "- The axis parameter specifies the axis along which the elements are removed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 5]\n",
      "[[1 3]\n",
      " [4 6]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "b = np.delete(a, [0, 2])\n",
    "print(b) \n",
    "\n",
    "c = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "d = np.delete(c, 1, axis=1)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **4. Resizing Arrays** \n",
    "##### np.resize(arr, new_shape): \n",
    "- This method resizes the arr array to the specified new_shape. \n",
    "- If the new shape is larger than the original array, new elements are filled with zeros."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 1]\n",
      " [2 3 4]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5])\n",
    "b = np.resize(a, (3, 3))\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hands-On Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **Array Operations and Broadcasting:**\n",
    "\n",
    "1. Given a 3D array a with shape (2, 3, 4) and a 2D array b with shape (3, 4), perform element-wise multiplication between a and b using broadcasting.\n",
    "2. Implement a function that takes two 2D arrays c and d with different shapes and performs element-wise operations (addition, subtraction, multiplication, and division) between them using broadcasting. Handle the case where broadcasting is not possible.\n",
    "3. Create a 2D array e with shape (5, 3) and a 1D array f with length 5. Compute the outer product of e and f using broadcasting.\n",
    "\n",
    "\n",
    "#### **Indexing and Slicing:**\n",
    "\n",
    "1. Given a 3D array g with shape (4, 3, 2), extract every other element along the first and second dimensions, but keep all elements along the third dimension.\n",
    "2. Create a function that takes a 2D array h and an array of row indices i and column indices j. The function should return a new array k where k[m, n] is the sum of the elements in h along the diagonal specified by i[m] and j[n].\n",
    "3. Implement a function that takes a 2D array l and returns a new array m where each element in m is the product of the corresponding row and column means in l.\n",
    "\n",
    "\n",
    "#### **Array Manipulation:**\n",
    "\n",
    "1. Given a 2D array n with shape (4, 6), reshape it into a 3D array with shape (2, 2, 6) and then flatten it back to a 2D array with shape (4, 6).\n",
    "2. Implement a function that takes a 2D array o and rolls it along the first axis by a specified number of positions. For example, if the input array is [[1, 2, 3], [4, 5, 6]] and the number of positions is 1, the output should be [[4, 5, 6], [1, 2, 3]].\n",
    "3. Create a function that takes a 2D array p and replaces all occurrences of a specified value x with the mean of the neighboring elements (horizontally and vertically) in the array."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}