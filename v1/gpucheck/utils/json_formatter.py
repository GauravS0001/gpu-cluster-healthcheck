import json


def format_json(results):

    payload = []

    for result in results:
        payload.append({
            "name": result.name,
            "status": result.status,
            "severity": result.severity,
            "message": result.message,
            "recommendation": result.recommendation
        })

    return json.dumps(payload, indent=2)