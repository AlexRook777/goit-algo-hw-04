from pathlib import Path
import argparse
import shutil

def parse_args():
    """
    Parse command line arguments.

    Returns an object containing the parsed arguments.

    The object will contain the following attributes:

    - source: Path to source directory.
    - dest: Path to destination directory. Default is "dist".
    """
    parser = argparse.ArgumentParser(description = "Copy files with sorting by extension.")
    parser.add_argument("--source", "-s",  type = Path, required = True, help = "Path to source directory.")
    parser.add_argument("--dest", "-d", type = Path, default = Path("dist"), help = "Path to destination directory.")
    return parser.parse_args()

def copy_files(src: Path, dest: Path) -> None:
    """
    Recursively copies files from source directory to destination directory, sorting by file extension.

    :param src: Path to source directory.
    :param dest: Path to destination directory.

    For each file in the source directory, a subdirectory is created in the destination
    directory with the same name as the file extension (without dot, e.g. "txt" for
    "example.txt"). If a file with the same name already exists in the subdirectory, a
    counter is added to the filename (e.g. "example_1.txt", "example_2.txt", etc.).

    If an exception occurs while copying a file, an error message is printed with the
    name of the file and the exception message.
    """
    for element in src.iterdir():
        if element.is_dir():
            copy_files(element, dest)
        else:
            try: # Moved try block inside the loop for granular exception handling
                ext = element.suffix.lstrip(".") or "no_extension"
                folder = dest / ext
                folder.mkdir(exist_ok = True, parents = True)

                target = folder / element.name
                counter = 1
                while target.exists():
                    stem = element.stem
                    suffix = element.suffix
                    target = folder / f"{stem}_{counter}{suffix}"
                    counter += 1

                shutil.copy(element, target)
                print(f"Copied {element} → {target}")

            except Exception as e:
                print(f"Error while copying {element}: {e}") # Error message now specific to the file


def main():
    """
    Main entry point of the script.

    Parses command line arguments, checks if the source directory exists and is a
    directory, and then copies files from the source directory to the destination
    directory, sorting by file extension.
    """
    args = parse_args()

    if not args.source.exists() or not args.source.is_dir():
        print(f"Source directory {args.source} does not exist or is not a directory.")
        return

    print(f"Copying files from {args.source} to {args.dest}...")
    copy_files(args.source, args.dest)
    print("Done.")

if __name__ == "__main__":
    main()
