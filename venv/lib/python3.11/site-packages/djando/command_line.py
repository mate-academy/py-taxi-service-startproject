import os.path
import shutil

PROJECT_DIR = os.path.dirname(__file__)


def main():
    print("Coping files to project...")
    shutil.copytree(os.path.join(PROJECT_DIR, 'data'), os.getcwd(), dirs_exist_ok=True)
