import subprocess

def check_k8s_nodes():
    try:
        output = subprocess.check_output(["kubectl", "get", "nodes"], timeout=2)
        return {"status": "healthy", "output": output.decode()}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}