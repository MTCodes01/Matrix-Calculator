# Matrix-Calculator

This project provides a set of functions to perform various matrix operations including addition, subtraction, multiplication, transpose, minor, cofactor, adjoint, determinant, and inverse. The project is divided into two main parts: the main script that handles user interaction and the module containing the matrix functions.

> [!NOTE]
> This is an improved version of my old program for matrix calculation that i did when i was starting to learn python 2 years ago, it was 1700+ lines of code(including the main and multiple module files combined)! and it was limited to only 3 by 3 matrices, so i really wanted to improve it, so 2 years later here i am after improving it from 1700+ lines of code to just 137 lines and it works with all sizes of matrices(Maybe depends on the device) but yea thats it, maybe i will try again after some time to shortening it and also try using new methods that I learn as I continue in this journey to learn more and try new things.

## Getting Started

### Prerequisites

- Python 3.x

Install [Python](https://www.python.org/), if you don't have python 3.x already installed.

### Installation

1. Clone the repository using the following in cmd/shell or just download the files.

   ```sh
   git clone https://github.com/MTCodes01/Matrix-Calculator.git
   ```
3. Ensure the `Matrix Calculator.py` and `Module/Mfunc.py` are in the correct directories.

### Running the Program

1. Open a terminal or command prompt.
2. Navigate to the directory containing `Matrix Calculator.py`.

   ```sh
   cd C:/path/to/your/directory
   ```
4. Run the program using the command:

   ```sh
   python Matrix Calculator.py
   ```
5. Follow the on-screen instructions to perform matrix operations.

## Main Script (Matrix Calculator.py)

The main script handles user interaction and calls the appropriate functions from the Mfunc module based on user input.

### Usage
1. When prompted, enter "Y" to start the program.
2. Choose the desired matrix operation by entering the corresponding number or name.
3. Enter the dimensions and elements of the matrices as prompted.
4. The result of the operation will be displayed.

### Operations

- Addition
- Difference (Subtraction)
- Multiplication
- Transpose
- Minor
- Cofactor
- Adjoint
- Determinant
- Inverse
- Exit

## Matrix Functions Module (Mfunc.py)

This module contains all the functions necessary to perform the matrix operations.

### Functions

- `inp(m1: int, n1: int, m2: int = 0, n2: int = 0)`: Prompts the user for matrix input. If `m2` and `n2` are provided, it takes input for two matrices; otherwise, it takes input for a single matrix.
- `out(lst: list[list[int]])`: Prints the matrix in a formatted way.
- `ADD(T: tuple[list[list[int]], list[list[int]]])`: Adds two matrices element-wise.
- `SUB(T: tuple[list[list[int]], list[list[int]]])`: Subtracts the second matrix from the first element-wise.
- `MUL(T: tuple[list[list[int]], list[list[int]]])`: Multiplies two matrices using matrix multiplication rules.
- `TRA(lst: list[list[int]]])`: Transposes the given matrix.
- `MIN(lst: list[list[int]], row: int = -1, col: int = -1)`: Calculates the minor of a matrix. If `row` and `col` are provided, it calculates the minor of the matrix at that position; otherwise, it returns the matrix of minors.
- `COF(lst: list[list[int]], row: int = -1, col: int = -1)`: Calculates the cofactor of a matrix. If `row` and `col` are provided, it calculates the cofactor of the matrix at that position; otherwise, it returns the matrix of cofactors.
- `DET(lst: list[list[int]]])`: Calculates the determinant of a matrix.
- `ADJ(lst: list[list[int]]])`: Calculates the adjoint (adjugate) of a matrix.
- `INV(lst: list[list[int]]])`: Calculates the inverse of a matrix, if the determinant is non-zero. Raises a `ZeroDivisionError` if the determinant is zero.

## Example

### Matrix Addition

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 1

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

B11: 5
B12: 6
B21: 7
B22: 8

6 8
10 12
```

### Matrix Subtraction

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 2

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 5
A12: 6
A21: 7
A22: 8

B11: 1
B12: 2
B21: 3
B22: 4

4 4
4 4
```

### Matrix Multiplication

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 3

Type 'm' by 'n' order of your Matrix: 
m1: 2
n1: 2

m2: 2
n2: 2

A11: 1
A12: 2
A21: 3
A22: 4

B11: 5
B12: 6
B21: 7
B22: 8

19 22
43 50
```

### Matrix Transpose

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 4

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

1 3
2 4
```

### Matrix Minor

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 5

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

4 3
2 1
```

### Matrix Cofactor

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 6

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

4 -3
-2 1
```

### Matrix Determinant

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 8

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

-2
```

### Matrix Adjoint

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 7

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

4 -2
-3 1
```

### Matrix Inverse

```vdnet
Enter "Y" to start!: Y

1) Addition
2) Difference
3) Multiplication
4) Transpose
5) Minor
6) Cofactor
7) Adjoint
8) Determinant
9) Inverse
10) Exit

Enter your option: 9

Type 'm' by 'n' order of your Matrix: 
m: 2
n: 2

A11: 1
A12: 2
A21: 3
A22: 4

-2.0  1.0
1.5 -0.5
```

<div align="center">
  Made by MTCode01, Just improved my 2 year old program!
</div>
