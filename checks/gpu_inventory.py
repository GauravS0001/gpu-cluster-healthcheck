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

        return output.decode()

    except Exception as e:

        return str(e)