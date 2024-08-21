import os


def sort_and_rename_csv(folder_path):
    # Get a list of CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    # Sort CSV files
    csv_files.sort()

    # Rename and move each CSV file with an incremental index
    for index, file_name in enumerate(csv_files, start=1):
        new_name = f"{index:02d}{file_name[2:]}"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} to {new_name}")


def process_folders(root_folder):
    for root, dirs, files in os.walk(root_folder):
        # Sort and rename CSV files in the current folder
        sort_and_rename_csv(root)


if __name__ == "__main__":
    root_folder = "."
    process_folders(root_folder)
    print("Done.")
