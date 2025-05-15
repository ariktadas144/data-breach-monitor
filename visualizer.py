import matplotlib.pyplot as plt
from datetime import datetime
failed_attempts = [
    "2025-05-15 10:10:00",
    "2025-05-15 10:12:00",
    "2025-05-15 10:12:00",
    "2025-05-15 10:15:00",
    "2025-05-15 10:20:00",
    "2025-05-15 10:20:00",
    "2025-05-15 10:20:00"
]

timestamps = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in failed_attempts]


from collections import Counter
time_keys = [ts.strftime("%H:%M") for ts in timestamps]
attempt_counts = Counter(time_keys)

sorted_times = sorted(attempt_counts)
counts = [attempt_counts[t] for t in sorted_times]

plt.figure(figsize=(8, 4))
plt.plot(sorted_times, counts, marker='o', linestyle='-', color='red')
plt.title("Failed Login Attempts Over Time")
plt.xlabel("Time (HH:MM)")
plt.ylabel("Number of Failed Attempts")
plt.grid(True)
plt.tight_layout()
plt.savefig("failed_attempts_plot.png")
plt.show()
