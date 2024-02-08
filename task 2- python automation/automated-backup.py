import shutil
import os

source_dir = pathtosource
destination_dir = pathtodestination

def backup()
    try
        shutil.copytree(source_dir, destination_dir)
        print(Backup successful)
    except Exception as e
        print(fBackup failed {e})

def main()
    backup()

if __name__ == __main__
    main()