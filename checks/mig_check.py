import subprocess


def check_mig():

    try:

        output = subprocess.check_output(
            [
                "nvidia-smi",
                "-L"
            ]
        )

        text = output.decode()

        enabled = "MIG" in text

        return {
            "status": "healthy",
            "mig_enabled": enabled
        }

    except Exception as e:

        return {
            "status": "failed",
            "details": str(e)
        }