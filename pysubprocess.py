import subprocess

# Example 1: subprocess.run()
def run_example():
    result = subprocess.run(["echo", "Hello from subprocess"], stdout=subprocess.PIPE, text=True)
    print("Example 1: using subprocess.run()")
    print("Return code:", result.returncode)
    print("Output:", result.stdout)
    print("")

# Example 2: subprocess.Popen()
def popen_example():
    process = subprocess.Popen(["echo", "Hello from Popen"], stdout=subprocess.PIPE, text=True)
    output, error = process.communicate()
    print("Example 2: using subprocess.Popen()")
    print("Return code:", process.returncode)
    print("Output:", output)
    print("")

# Example 3: subprocess.call()
def call_example():
    return_code = subprocess.call(["echo", "Hello from call"])
    print("Example 3: using subprocess.call()")
    print("Return code:", return_code)
    print("")

# Example 4: subprocess.check_output()
def check_output_example():
    output = subprocess.check_output(["echo", "Hello from check_output"], text=True)
    print("Example 4: using subprocess.check_output()")
    print("Output:", output)
    print("")

# Running all examples
run_example()
popen_example()
call_example()
check_output_example()
