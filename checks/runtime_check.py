import subprocess


def check_container_runtime():

    try:

        output = subprocess.check_output(
            ["docker", "info"]
        )

        return "Docker Runtime Healthy"

    except Exception as e:

        return str(e)