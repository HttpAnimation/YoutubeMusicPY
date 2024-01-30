import subprocess
import sys

def install_dependencies():
    required_dependencies = ['requests', 'pygame', 'pafy', 'youtube_dl']

    optional_dependencies = ['youtube-dl', 'mutagen', 'Pillow']

    # Install required dependencies
    for dependency in required_dependencies:
        install_command = [sys.executable, '-m', 'pip', 'install', dependency]
        subprocess.run(install_command, check=True)

    # Install optional dependencies
    for dependency in optional_dependencies:
        install_command = ['pip', 'install', dependency]
        subprocess.run(install_command, check=True)

if __name__ == "__main__":
    install_dependencies()
