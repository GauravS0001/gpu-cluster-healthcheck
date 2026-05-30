import subprocess


def check_cuda():

    try:

        output = subprocess.check_output(
            ["nvcc", "--version"]
        )

        return output.decode()

    except Exception as e:

        return str(e)