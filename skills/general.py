import os
import sys

# For Windows volume control
try:
    import ctypes
except ImportError:
    ctypes = None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "Console cleared."

def set_volume(level):
    """Set master volume (0-100) on Windows."""
    if ctypes is None:
        return "Volume control not supported on this system."
    try:
        devices = ctypes.windll.winmm.waveOutSetVolume
        # level: 0 (mute) to 100 (max)
        volume = int(level * 65535 / 100)
        devices(0, volume + (volume << 16))
        return f"Volume set to {level}%."
    except Exception:
        return "Failed to set volume."

def change_volume(delta):
    """Increase or decrease volume by delta."""
    if ctypes is None:
        return "Volume control not supported on this system."
    try:
        # Get current volume
        current = ctypes.c_ulong()
        ctypes.windll.winmm.waveOutGetVolume(0, ctypes.byref(current))
        left = current.value & 0xFFFF
        right = (current.value >> 16) & 0xFFFF
        avg = int((left + right) / 2)
        percent = int(avg * 100 / 65535)
        new_percent = min(100, max(0, percent + delta))
        return set_volume(new_percent)
    except Exception:
        return "Failed to change volume."

def mute_volume():
    return set_volume(0)

def max_volume():
    return set_volume(100)