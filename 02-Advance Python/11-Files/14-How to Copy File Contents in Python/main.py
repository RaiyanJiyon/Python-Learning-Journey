def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, "r") as src_file:
            # Open the destination file for writing
            with open(destination_file, "w") as dest_file:
                # Read the contents of the source file
                contents = src_file.read()
                # Write the contents to the destination file
                dest_file.write(contents)
        print("File copied successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
copy_file("source.txt", "destination.txt")
