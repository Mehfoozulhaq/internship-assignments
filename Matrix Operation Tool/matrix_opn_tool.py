import tkinter as tk
from tkinter import messagebox
import numpy as np


def parse_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except:
        raise ValueError("Invalid format")


def display_result(result):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(result))


def add_matrices():
    try:
        A = parse_matrix(matrix_a_text.get("1.0", tk.END))
        B = parse_matrix(matrix_b_text.get("1.0", tk.END))
        if A.shape != B.shape:
            raise ValueError("Dimensions don't match")
        display_result(A + B)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def subtract_matrices():
    try:
        A = parse_matrix(matrix_a_text.get("1.0", tk.END))
        B = parse_matrix(matrix_b_text.get("1.0", tk.END))
        if A.shape != B.shape:
            raise ValueError("Dimensions don't match")
        display_result(A - B)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def multiply_matrices():
    try:
        A = parse_matrix(matrix_a_text.get("1.0", tk.END))
        B = parse_matrix(matrix_b_text.get("1.0", tk.END))
        if A.shape[1] != B.shape[0]:
            raise ValueError("Incompatible dimensions")
        display_result(np.dot(A, B))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def transpose_matrix():
    try:
        A = parse_matrix(matrix_a_text.get("1.0", tk.END))
        display_result(A.T)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def determinant_matrix():
    try:
        A = parse_matrix(matrix_a_text.get("1.0", tk.END))
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square")
        det = np.linalg.det(A)
        display_result(f"Determinant: {det:.4f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("700x500")

tk.Label(root, text="Matrix A", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Matrix B", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Result", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10, pady=5)
matrix_a_text = tk.Text(root, height=10, width=20)
matrix_b_text = tk.Text(root, height=10, width=20)
result_text = tk.Text(root, height=10, width=20)

matrix_a_text.grid(row=1, column=0, padx=10)
matrix_b_text.grid(row=1, column=1, padx=10)
result_text.grid(row=1, column=2, padx=10)

button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=3, pady=20)

tk.Button(button_frame, text="Add", width=15, command=add_matrices).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Subtract", width=15, command=subtract_matrices).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Multiply", width=15, command=multiply_matrices).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Transpose", width=15, command=transpose_matrix).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Determinant", width=15, command=determinant_matrix).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
