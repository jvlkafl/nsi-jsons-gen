import os
import shutil

def generate_folder_names(problem, bias_values, ahln_values, y_values):
    folder_names = []
    for bias in bias_values:
        for ahln in ahln_values:
            for y in y_values:
                folder_name = f"NSI_p{problem}_{bias}_{ahln}_{y}"
                folder_names.append(folder_name)
    return folder_names

def copy_folders_with_names(source_folder, target_folder, folder_names):
    try:
        # Create the target folder if it doesn't exist
        os.makedirs(target_folder, exist_ok=True)

        # Copy the source folder to the target folder with different names
        for folder_name in folder_names:
            target_path = os.path.join(target_folder, folder_name)
            shutil.copytree(source_folder, target_path)
            print(f"Folder '{folder_name}' created successfully.")

    except Exception as e:
        print(f"Error: {e}")

def main():
    source_folder = r"C:\Users\Lenovo\Desktop\jsons\NSI template" ## change to your own
    target_folder = r"C:\Users\Lenovo\Desktop\jsons\p13_f" ## change to your own

    problem = 13
    bias_values = [-6, -2, -1.5, -1, -0.5, -0.1, -0.01, 0, 0.01, 0.1, 0.5, 1, 1.5, 2, 6]
    ahln_values = [10.0, 7.0, 5.0, 2.0, 1.0, 0.0]
    y_values = [1]

    folder_names = generate_folder_names(problem, bias_values, ahln_values, y_values)

    copy_folders_with_names(source_folder, target_folder, folder_names)

if __name__ == "__main__":
    main()
