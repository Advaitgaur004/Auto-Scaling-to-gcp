import requests
import subprocess
import time
import os

PROMETHEUS_URL = "http://localhost:9090/api/v1/query"
CPU_THRESHOLD = 75  # 75% threshold
GCP_PROJECT = "gcc-ass-3"
GCP_ZONE = "asia-south1-a" 
GCP_INSTANCE = "ubuntu-cloud-vm-india"
GCP_MACHINE_TYPE = "e2-standard-8" 

def get_cpu_usage():
    query = '100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'
    response = requests.get(PROMETHEUS_URL, params={'query': query})
    result = response.json()['data']['result']
    if result:
        return float(result[0]['value'][1])
    return 0

def launch_gcp_instance():
    cmd = f"gcloud compute instances create {GCP_INSTANCE} --zone={GCP_ZONE} --machine-type={GCP_MACHINE_TYPE} --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Launched {GCP_INSTANCE} in GCP zone {GCP_ZONE} with {GCP_MACHINE_TYPE}.")

def main():
    while True:
        cpu_usage = get_cpu_usage()
        print(f"Current CPU Usage: {cpu_usage:.2f}%")
        if cpu_usage > CPU_THRESHOLD:
            print(f"CPU usage exceeds {CPU_THRESHOLD}%. Scaling to GCP in India region...")
            launch_gcp_instance()
            break
        time.sleep(5)  # Check every 5 sec

if __name__ == "__main__":
    main()
