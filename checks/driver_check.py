import subprocess


def check_driver():

    try:

        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=driver_version",
                "--format=csv,noheader"
            ]
        )

        return {
            "status": "healthy",
            "version": output.decode().strip()
        }

    except Exception as e:

        return {
            "status": "failed",
            "version": str(e)
        }