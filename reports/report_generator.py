import json


def generate_report(results):

    with open(
        "sample-output/health-report.json",
        "w"
    ) as f:

        json.dump(
            results,
            f,
            indent=4
        )

    with open(
        "sample-output/health-report.txt",
        "w"
    ) as f:

        for key, value in results.items():

            f.write(f"{key}\n")
            f.write(f"{value}\n\n")