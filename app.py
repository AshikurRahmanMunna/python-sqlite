"""send email python"""
import subprocess

try:
    completed = subprocess.run(
        ["python", "other1.py"], check=False, capture_output=True, text=True)
    print(completed.args)
    print(completed.stderr)
    print(completed.stdout)
    print(completed.returncode)
except ChildProcessError as ex:
    print(ex)
