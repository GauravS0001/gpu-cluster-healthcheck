import subprocess


def check_device_plugin():

    try:

        output = subprocess.check_output(
            [
                "kubectl",
                "get",
                "pods",
                "-n",
                "kube-system"
            ]
        )

        return output.decode()

    except Exception as e:

        return str(e)