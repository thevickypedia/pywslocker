import ctypes
import os

from .module import settings


def lock():
    """Locks the workstation."""
    if settings.os == "Darwin":
        os.system(
            """osascript -e 'tell application "System Events" to keystroke "q" using {control down, command down}'"""
        )
    elif settings.os == "Windows":
        ctypes.windll.user32.LockWorkStation()
    else:
        os.system("gnome-screensaver-command --lock")
