import subprocess


def get_gpu_inventory():

    try:

        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total",
                "--format=csv,noheader"
            ]
        )

        return {
            "status": "healthy",
            "details": output.decode().strip()
        }

    except Exception as e:

        return {
            "status": "failed",
            "details": str(e)
        }