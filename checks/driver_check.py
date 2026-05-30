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

        return output.decode()

    except Exception as e:

        return str(e)