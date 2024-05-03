import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        super().__init__()
        self.command = command

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.py'):
            print(f"Python file {event.src_path} has been modified")
            self.run_command()

    def run_command(self):
        try:
            subprocess.run(self.command, shell=True, check=True)
            print("Command executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def watch_directory(directory, command):
    event_handler = FileChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) < 3:

        print("Usage: python watch_directory.py <directory_to_watch> <command_to_execute>")
        sys.exit(1)
    
    directory = sys.argv[1]
    command = sys.argv[2]

    watch_directory(directory, command)
