# microsoft-Office
import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes, seconds = divmod(remaining_time, 60)
        print(f"Time remaining: {int(minutes)} minutes {int(seconds)} seconds", end="\r")
        time.sleep(1)
    print("\nTime's up! Take a break.")

if __name__ == "__main__":
    focus_duration = int(input("Enter focus duration in minutes: "))
    focus_timer(focus_duration * 60)
