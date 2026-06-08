
import traceback
import sys

for thread_id, frame in sys._current_frames().items():
    print(f"\n=== Поток ID: {thread_id} ===")
    traceback.print_stack(frame)
