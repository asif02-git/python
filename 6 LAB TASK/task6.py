# Task 6: Challenge Mini Log Parser
import re
from collections import Counter

log_data = """[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"
[2024-06-01 08:18:10] ERROR user=agarcia msg="Connection timeout"
[2024-06-01 08:19:00] ERROR user=jsmith msg="Database connection failed"
"""

# 1. Regex pattern with named groups
log_pattern = r"\[(?P<timestamp>[^\]]+)\]\s+(?P<level>\w+)\s+user=(?P<user>\w+)\s+msg=\"(?P<msg>[^\"]+)\""

# 2. Build list of dicts using finditer() and groupdict()
entries = [match.groupdict() for match in re.finditer(log_pattern, log_data)]
print("Task 6.1 & 6.2 - Parsed Entries (First 2 shown):")
for entry in entries[:2]:
    print(" ", entry)

# 3. Summary count of log levels
counts = Counter(entry['level'] for entry in entries)
print("\nTask 6.3 - Log Level Counts:")
print(f"  ERROR: {counts['ERROR']}, WARN: {counts['WARN']}, INFO: {counts['INFO']}")

# 4. Redact user names using re.sub()
redacted_logs = re.sub(r"user=\w+", "user=<hidden>", log_data)
print("\nTask 6.4 - Redacted Log Output:")
print(redacted_logs)

# Bonus: Sort entries by user name and print only ERROR entries
print("Task 6 Bonus - Sorted ERROR entries per user:")
sorted_entries = sorted(entries, key=lambda x: x['user'])
for entry in sorted_entries:
    if entry['level'] == 'ERROR':
        print(f"  User: {entry['user']} | Time: {entry['timestamp']} | Msg: {entry['msg']}")

# Task 6.1 & 6.2 - Parsed Entries (First 2 shown):
#   {'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
#   {'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}

# Task 6.3 - Log Level Counts:
#   ERROR: 3, WARN: 1, INFO: 1

# Task 6.4 - Redacted Log Output:
# [2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
# [2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
# [2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"
# [2024-06-01 08:18:10] ERROR user=<hidden> msg="Connection timeout"
# [2024-06-01 08:19:00] ERROR user=<hidden> msg="Database connection failed"

# Task 6 Bonus - Sorted ERROR entries per user:
#   User: agarcia | Time: 2024-06-01 08:18:10 | Msg: Connection timeout
#   User: jsmith | Time: 2024-06-01 08:15:32 | Msg: Disk quota exceeded
#   User: jsmith | Time: 2024-06-01 08:19:00 | Msg: Database connection failed
