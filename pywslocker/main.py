import os
import subprocess

from .module import settings


def lock():
    """Locks the workstation."""
    if settings.os == "Darwin":
        os.system(
            """osascript -e 'tell application "System Events" to keystroke "q" using {control down, command down}'"""
        )
    elif settings.os == "Windows":
        try:
            import ctypes
            ctypes.windll.user32.LockWorkStation()
        except (ImportError, AttributeError):
            subprocess.call('rundll32.exe user32.dll, LockWorkStation')
    else:
        os.system("gnome-screensaver-command --lock")
