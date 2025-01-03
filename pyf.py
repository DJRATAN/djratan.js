import requests
import os

def download_file(url, destination_folder):
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_path = os.path.join(destination_folder, file_name)
        
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Downloaded {file_name} to {file_path}")
    else:
        print(f"Failed to download the file from {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    file_url = input("Enter the URL of the file you want to download: ")
    download_folder = input("Enter the destination folder path (Press Enter to use the current directory): ")

    if download_folder == "":
        download_folder = os.getcwd()
    elif not os.path.exists(download_folder):
        os.makedirs(download_folder)

    download_file(file_url, download_folder)
