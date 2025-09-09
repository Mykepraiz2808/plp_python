# 📝 File Read & Write + Error Handling Program

def modify_file(input_file, output_file):
    """Read from input_file, modify the content, and write to output_file."""
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # Example modification: make text uppercase
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"🚫 Error: No permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def read_user_file():
    """Ask the user for a filename and try to read it with error handling."""
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            print("\n📖 File content:\n")
            print(f.read())

    except FileNotFoundError:
        print(f"❌ Error: '{filename}' not found.")
    except PermissionError:
        print(f"🚫 Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# === Main Program ===
if __name__ == "__main__":
    input_file = input("Enter the input filename: ")
    output_file = "modified_output.txt"  # You can customize the output name

    modify_file(input_file, output_file)

    print("\n--- Now let’s try reading a file ---")
    read_user_file()
