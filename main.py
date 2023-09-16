import argparse
import fileinput

def find_replace_in_files(files, find_str, replace_str):
    for line in fileinput.input(files, inplace=True):
        line = line.replace(find_str, replace_str)
        print(line, end='')

def main():
    parser = argparse.ArgumentParser(description="Find and replace content in files.")
    parser.add_argument('files', nargs='+', help='List of files to search and replace in')
    parser.add_argument('--find', required=True, help='Text to find in the files')
    parser.add_argument('--replace', required=True, help='Text to replace the found text with')

    args = parser.parse_args()

    find_replace_in_files(args.files, args.find, args.replace)

if __name__ == "__main__":
    main()
