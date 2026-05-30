import subprocess


def check_memory():

    try:

        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=memory.used,memory.total",
                "--format=csv,noheader,nounits"
            ]
        )

        line = output.decode().splitlines()[0]

        used, total = line.split(",")

        used = int(used.strip())
        total = int(total.strip())

        percent = round((used / total) * 100, 2)

        status = "healthy"

        if percent > 90:
            status = "warning"

        return {
            "status": status,
            "memory_used_mb": used,
            "memory_total_mb": total,
            "usage_percent": percent
        }

    except Exception as e:

        return {
            "status": "failed",
            "details": str(e)
        }