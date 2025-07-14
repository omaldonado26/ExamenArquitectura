# sistema/utils/system_info.py

import psutil
import platform

def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=0.5)
    except Exception as e:
        return f"Error: {e}"

def get_memory_info():
    try:
        mem = psutil.virtual_memory()
        return {
            'total_gb': round(mem.total / (1024**3), 2),
            'used_gb':  round(mem.used  / (1024**3), 2),
            'percent':  mem.percent,
        }
    except Exception as e:
        return {'error': str(e)}

def get_disk_info():
    try:
        disk = psutil.disk_usage('/')
        return {
            'total_gb': round(disk.total / (1024**3), 2),
            'used_gb':  round(disk.used  / (1024**3), 2),
            'free_gb':  round(disk.free  / (1024**3), 2),
            'percent':  disk.percent,
        }
    except Exception as e:
        return {'error': str(e)}

def get_system_info():
    try:
        return {
            'os':               platform.system() + ' ' + platform.release(),
            'cores_logical':    psutil.cpu_count(logical=True),
            'cores_physical':   psutil.cpu_count(logical=False),
        }
    except Exception as e:
        return {'error': str(e)}
