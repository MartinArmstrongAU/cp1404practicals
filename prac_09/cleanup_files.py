import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)

        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    fixed_filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    previous_char = ""
    new_filename = ""
    for character in fixed_filename:
        if previous_char.islower():
            if character.isupper():
                new_filename += "_"
        if previous_char == "_":
            character = character.upper()
        new_filename += character
        previous_char = character
    return new_filename


def demo_walk():
    """Return a 'fixed' version of filename."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)

        # for filename in filenames:
        #     try:
        #         new_filename = os.path.join(directory_name, filename)
        #         fixed_filename = get_fixed_filename(new_filename)
        #         os.rename(new_filename, fixed_filename)
        #     except FileExistsError:
        #         pass

#demo_walk()
main()
