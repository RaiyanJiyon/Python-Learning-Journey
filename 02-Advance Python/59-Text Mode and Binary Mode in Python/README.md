# Text Mode and Binary Mode in Python

In Python file handling, both text mode and binary mode specify how files are read from or written to. These modes determine how the data is interpreted and processed by Python. Here's an explanation of text mode and binary mode:

## Text Mode ("t")
Text mode is the default mode when opening a file in Python. In text mode, files are treated as a sequence of characters, and data is encoded and decoded automatically to ensure compatibility with the character encoding used by the system (typically UTF-8).

When reading from a file in text mode ("rt"), newline characters ('\n') are automatically translated to the appropriate line ending character(s) for the platform ('\r\n' on Windows, '\n' on Unix-like systems). Similarly, when writing to a file in text mode ("wt"), newline characters are converted to the platform-specific line endings.

## Binary Mode ("b")
Binary mode, denoted by "b", is used when working with files that contain non-textual data, such as images, audio files, or executable programs. In binary mode, files are treated as a sequence of bytes, and no automatic encoding or decoding of data is performed.

When reading from a file in binary mode ("rb"), data is read exactly as it is stored on disk, without any modifications. Similarly, when writing to a file in binary mode ("wb"), data is written to the file without any encoding or newline translation.

### Text Mode:

```python
f = open('Student.txt', mode='w')
f.write("MD. Raiyan Ur Rahman\n")
f.write("221902113\n")
f.write('CSE\n')
f.write('Male\n')
f.close()
print("File is Created")

f = open('Student.txt', mode='r')
data = f.read()
print(data)
f.close()
```

### Binary Mode:

```python
f = open('Student.txt', mode='rb')
binary = f.read()
print(binary)
f.close()
```

When working with files, it's essential to choose the appropriate mode based on the type of data you are dealing with. Text mode is suitable for textual data, while binary mode is ideal for non-textual data or when you need to preserve the exact byte representation of the data.