# Subprocess to execute external commands
# Main arguments of subprocess.run():
# - stdout, stdin, and stderr -> Redirect output, input, and errors
# - capture_output -> Capture output and error for later use
# - text -> If True, inputs and outputs are treated as text
# and automatically encoded or decoded with the platform's
# default character set (usually UTF-8).
# - shell -> If True, allows access to the system shell. When
# using shell (True), it is recommended to send the command
# and arguments together.
# - executable -> can be used to specify the path of the
# executable that will start the subprocess.
# Return:
# stdout, stderr, returncode, and args
import subprocess
import sys

# sys.platform = linux, linux2, darwin, win32
system = sys.platform
# print(system)


command = ['ping', '127.0.0.1']

if system == "win32":
    command = ['ping', '127.0.0.1']
    encoding = 'cp850'

process = subprocess.run(
    command, capture_output=True,
    text=True, encoding=encoding,
)

print()
# print(process.args)
# print(process.stderr)
# print(process.stdout.decode('cp850')) # This may change depending on your OS
print(process.stdout)
# print(process.returncode)