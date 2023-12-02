import os
import shutil

if __name__ == "__main__":
    user = os.getlogin()
    downloadFolder = fr'C:\Users\{user}\Downloads'
    fileTypes = ['Picture', 'Video', 'Audio', 'Torrents', 'Docs', 'Executables', 'Archives']
    outputFolders = {
        'Picture': r'D:\Pictures',
        'Video': r'D:\Videos',
        'Audio': r'D:\Audio',
        'Torrents': r'D:\Torrents',
        'Docs': r'D:\Docs',
        'Executables': r'D:\Executables',
        'Archives': r'D:\Archives'
    }
    fileTypesDict = {
        'Picture': ['.png', '.jpeg', '.jpg', '.webp', '.gif'],
        'Video': ['.mp4'],
        'Audio': ['.mp3'],
        'Torrents': ['.torrent'],
        'Docs': ['.pdf', '.docx', '.pptx'],
        'Executables': ['.exe'],
        'Archives': ['.zip', '.7z', '.rar']
    }

    source = os.listdir(downloadFolder)
    for file in source:
        for fileType in fileTypes:
            if not os.path.exists(outputFolders[fileType]):
                os.makedirs(outputFolders[fileType])
            if file.endswith(tuple(fileTypesDict[fileType])):
                shutil.move(os.path.join(downloadFolder, file), os.path.join(outputFolders[fileType], file))
                print(f'Moved {os.path.join(downloadFolder, file)} to {os.path.join(outputFolders[fileType], file)}')
    
    print('Done!')