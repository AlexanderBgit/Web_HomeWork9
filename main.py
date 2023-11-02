import os
import subprocess

# Виконання скрипту для отримання інформації та створення JSON-файлів
subprocess.run(["python", "bsoup.py"])

# Виконання скрипту для завантаження JSON-файлів у хмарну базу даних MongoDB
subprocess.run(["python", "add.py"])
