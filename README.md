## DSA-HW02--Sparse-Matrix

To ensure the folder structure is displayed correctly in the README.md file, you need to format it using Markdown code blocks. Here's the corrected section of your README.md file with proper formatting:

```markdown
# Sparse Matrix Operations

This project allows you to perform operations (addition, subtraction, multiplication) on sparse matrices using Python.

## Folder Structure

```
DSA-HW02--Sparse-Matrix/
│
├── code/
│   ├── src/
│   │   └── sparse_matrix.py
│
├── outputs/
│   ├── easy_sample_01.txt
│   └── easy_sample_02.txt
│   ├── ...
│
├── sample_inputs/
│   ├── easy_sample_01_1.txt
│   └── easy_sample_01_2.txt
│   ├── easy_sample_01_3.txt
│   └── ...
│
└── README.md
```

## Prerequisites

- Python 3.x

## Usage

Clone the repository:
```sh
git clone "https://github.com/Jules-gatete/DSA-HW02--Sparse-Matrix.git"
```

Navigate to the project directory:
```sh
cd DSA-HW02--Sparse-Matrix
```

Ensure your input files are in the `sample_inputs` directory.

Run the script:
```sh
python code/src/sparse_matrix.py <operation> <inputFile1> <inputFile2> <outputFile>
```

For example:
```sh
python code/src/sparse_matrix.py add easy_sample_01_1.txt easy_sample_01_2.txt easy_sample_01.txt
```

The result will be saved in the `outputs` directory.

## Input File Format

The input files should have the following format:

```
rows=3
cols=3
0 0 1
1 2 2
2 1 3
```

## Output

The result of the operation will be saved in the specified output file.

## Notes

Ensure the matrices conform to the mathematical rules for the selected operation.
Handle file paths and ensure input files exist in the specified directory.
```

By using the triple backticks (```) before and after the folder structure, it will be displayed as a code block, preserving the intended formatting. This way, the folder structure will be clear and easy to understand.


By following the above steps, you'll have a Python-based project capable of performing sparse matrix operations. The provided code reads the sparse matrix data from files, performs the specified operation, and writes the result back to an output file.
