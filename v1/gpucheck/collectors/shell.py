import subprocess


def run_command(command: str):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }

    except Exception as e:
        return {
            "returncode": 1,
            "stdout": "",
            "stderr": str(e)
        }