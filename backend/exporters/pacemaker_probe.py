import subprocess

def check_pacemaker():
    try:
        output = subprocess.check_output(["crm_mon", "-1"], timeout=2)
        return {"status": "healthy", "output": output.decode()}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
