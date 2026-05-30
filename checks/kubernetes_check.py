from kubernetes import client
from kubernetes import config


def check_kubernetes():

    try:

        config.load_kube_config()

        v1 = client.CoreV1Api()

        nodes = v1.list_node()

        node_data = []

        for node in nodes.items:

            ready = False

            for condition in node.status.conditions:

                if (
                    condition.type == "Ready"
                    and condition.status == "True"
                ):
                    ready = True

            node_data.append(
                {
                    "node": node.metadata.name,
                    "ready": ready
                }
            )

        return {
            "status": "healthy",
            "nodes": node_data
        }

    except Exception as e:

        return {
            "status": "failed",
            "details": str(e)
        }