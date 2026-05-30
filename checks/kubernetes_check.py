import subprocess


def check_nodes():

    try:

        output = subprocess.check_output(
            [
                "kubectl",
                "get",
                "nodes"
            ]
        )

        return output.decode()

    except Exception as e:

        return str(e)