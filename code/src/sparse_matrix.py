import os

class SparseMatrix:
    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        self.elements = elements if elements else {}

    @staticmethod
    def from_file(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            rows = int(lines[0].split('=')[1])
            cols = int(lines[1].split('=')[1])
            elements = {}
            for line in lines[2:]:
                row, col, value = map(int, line.split())
                elements[(row, col)] = value
            return SparseMatrix(rows, cols, elements)

    def to_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f'rows={self.rows}\n')
            f.write(f'cols={self.cols}\n')
            for (row, col), value in self.elements.items():
                f.write(f'{row} {col} {value}\n')

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrix dimensions must match for addition')

        result_elements = self.elements.copy()
        for (row, col), value in other.elements.items():
            if (row, col) in result_elements:
                result_elements[(row, col)] += value
            else:
                result_elements[(row, col)] = value
        return SparseMatrix(self.rows, self.cols, result_elements)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrix dimensions must match for subtraction')

        result_elements = self.elements.copy()
        for (row, col), value in other.elements.items():
            if (row, col) in result_elements:
                result_elements[(row, col)] -= value
            else:
                result_elements[(row, col)] = -value
        return SparseMatrix(self.rows, self.cols, result_elements)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError('Matrix dimensions must match for multiplication')

        result_elements = {}
        for (rowA, colA), valueA in self.elements.items():
            for (rowB, colB), valueB in other.elements.items():
                if colA == rowB:
                    if (rowA, colB) in result_elements:
                        result_elements[(rowA, colB)] += valueA * valueB
                    else:
                        result_elements[(rowA, colB)] = valueA * valueB
        return SparseMatrix(self.rows, other.cols, result_elements)

def main():
    import sys
    if len(sys.argv) != 5:
        print("Usage: python sparse_matrix.py <operation> <inputFile1> <inputFile2> <outputFile>")
        return

    operation = sys.argv[1]
    input_file1 = os.path.join('../../sample_inputs', sys.argv[2])
    input_file2 = os.path.join('../../sample_inputs', sys.argv[3])
    output_file = os.path.join('../../outputs', sys.argv[4])

    matrix1 = SparseMatrix.from_file(input_file1)
    matrix2 = SparseMatrix.from_file(input_file2)

    if operation == 'add':
        result = matrix1.add(matrix2)
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation. Use add, subtract, or multiply.")
        return

    result.to_file(output_file)
    print(f'Result saved to {output_file}')

if __name__ == '__main__':
    main()
