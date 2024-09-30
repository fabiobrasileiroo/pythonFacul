from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class MyHandler(FileSystemEventHandler):
    def __init__(self, file_to_watch):
        self.file_to_watch = file_to_watch

    def on_modified(self, event):
        if event.src_path.endswith(self.file_to_watch):
            print(f'{self.file_to_watch} foi modificado. Executando novamente...')
            os.system(f'python {self.file_to_watch}')

if __name__ == "__main__":
    file_to_watch = '01.py'  # Substitua pelo nome do arquivo que deseja monitorar
    event_handler = MyHandler(file_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
