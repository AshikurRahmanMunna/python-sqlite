"""send email python"""
import subprocess

completed = subprocess.run(
    ["python", "other1.py"], check=False, capture_output=True, text=True)

print(completed.returncode)
if completed.returncode == 0:
    print(completed.stdout)
else:
    print(completed.stderr)
