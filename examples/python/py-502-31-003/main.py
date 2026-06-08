from pathlib import Path

import time

def cleanup_logs(log_dir, days=30):
    log_path = Path(log_dir)
    cutoff = time.time() - (days * 86400)  # 86400 секунд в сутках
    
    for logfile in log_path.glob('*.log'):
        if logfile.stat().st_mtime < cutoff:
            print(f"Удаление {logfile}")
            logfile.unlink()

cleanup_logs('/var/log/myapp', days=7)
