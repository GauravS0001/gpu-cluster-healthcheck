def calculate_score(results):

    score = 100

    issues = []

    if results["driver"]["status"] != "healthy":
        score -= 20
        issues.append("driver_failure")

    if results["cuda"]["status"] != "healthy":
        score -= 20
        issues.append("cuda_failure")

    if results["runtime"]["status"] != "healthy":
        score -= 15
        issues.append("runtime_failure")

    if results["kubernetes"]["status"] != "healthy":
        score -= 15
        issues.append("kubernetes_failure")

    if results["memory"]["status"] == "warning":
        score -= 10
        issues.append("high_memory_usage")

    if score >= 90:
        state = "HEALTHY"

    elif score >= 70:
        state = "WARNING"

    else:
        state = "CRITICAL"

    return {
        "cluster_score": score,
        "status": state,
        "issues": issues
    }