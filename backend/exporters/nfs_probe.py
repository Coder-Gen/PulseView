import os

def check_nfs_health():
    path = os.getenv("NFS_PROBE_PATH", "/mnt/app_data/healthcheck.txt")
    return os.path.isfile(path)