import subprocess


def check_cuda():

    try:

        output = subprocess.check_output(
            [
                "nvcc",
                "--version"
            ]
        )

        return {
            "status": "healthy",
            "details": output.decode()
        }

    except Exception as e:

        return {
            "status": "failed",
            "details": str(e)
        }