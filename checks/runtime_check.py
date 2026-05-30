import subprocess


def check_runtime():

    try:

        subprocess.check_output(
            [
                "docker",
                "info"
            ]
        )

        return {
            "status": "healthy"
        }

    except Exception as e:

        return {
            "status": "failed",
            "details": str(e)
        }