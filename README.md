# Local VM Auto-Scaling to GCP Based on Resource Usage

I developed this project to create a local virtual machine (VM) using VirtualBox and Ubuntu, with an auto-scaling mechanism to Google Cloud Platform (GCP) based on CPU resource usage. When the CPU usage exceeds 75%, the system automatically triggers the creation of a new GCP instance. The project integrates Prometheus and Node Exporter for monitoring, a custom Python script for decision-making, and the Google Cloud CLI for cloud scaling.

## Architecture

The overall architecture consists of the following components:

- **Local VM:** Runs Ubuntu on VirtualBox.
- **Monitoring:** Prometheus and Node Exporter monitor system metrics.
- **Auto-Scaling Mechanism:** A Python script (available in the codebase) queries Prometheus to check CPU usage and triggers scaling if necessary.
- **GCP Integration:** Uses Google Cloud CLI to create a new instance when the CPU threshold is exceeded.

### Architecture Diagram

I have included an architecture diagram in the project repository that visually represents this setup.

## Prerequisites

- **VirtualBox:** Installed from [VirtualBox Official Site](https://www.virtualbox.org).
- **Ubuntu 22.04 LTS ISO:** Downloaded from [Ubuntu Official Site](https://ubuntu.com/download).
- **Google Cloud CLI:** Installed and authenticated using `gcloud init`.
- **Prometheus and Node Exporter:** Set up for system monitoring.
- **Python 3.x:** Required to run the auto-scaling script (the code is available in the codebase).

## Installation and Setup

### 1. Creating a Local VM

1. **Download and Install VirtualBox:** Get it from the [VirtualBox website](https://www.virtualbox.org).
2. **Download Ubuntu 22.04 LTS:** Available on [Ubuntu's download page](https://ubuntu.com/download).
3. **Create a New VM with the Following Settings:**
   - **Name:** Ubuntu-VM
   - **Type:** Linux, **Version:** Ubuntu (64-bit)
   - **RAM:** 6.5GB (6480MB)
   - **CPU:** 8 processors
   - **Disk:** 25GB (VDI, dynamically allocated)
   - **Network:** NAT using Intel PRO/1000 MT Desktop
   - **Graphics:** VMSVGA with 16MB Video Memory
   - **Audio:** ICH AC97
   - **USB Controller:** OHCI, EHCI
   - **Guest Additions:** VBoxGuestAdditions.iso for enhanced features

### 2. Setting Up Resource Monitoring

1. **Node Exporter:**
   - Download from GitHub and move the binary to `/usr/local/bin/`.
   - Configure it as a systemd service running on port `9100`.

2. **Prometheus:**
   - Download and configure Prometheus with a scrape interval of 15 seconds.
   - Configure it to scrape metrics from Node Exporter at `localhost:9100`.
   - Verify the setup via the Prometheus UI at `http://10.0.2.15:9090`.

### 3. Configuring Cloud Auto-Scaling to GCP

1. **GCP Setup:**
   - Create a GCP account and a project named "auto-scale-demo".
   - Enable the Compute Engine API.
   - Install and configure the Google Cloud CLI (`gcloud init`).

2. **Auto-Scaling Script:**
   - A Python script in the codebase monitors CPU usage and triggers a new GCP instance when usage exceeds 75%.
   - The script queries Prometheus, checks CPU usage, and uses the Google Cloud CLI to launch a new instance.
   - The Python code is already included in the codebase, so please refer to that for implementation details.

### 4. Testing

1. **Deploy Nginx:** Install Nginx as a sample application on the VM.
2. **Simulate High CPU Usage:** Use the `stress` tool to simulate high CPU load.
3. **Verify Scaling:** Monitor the terminal output and Prometheus UI to ensure that a new GCP instance is launched when the CPU usage exceeds 75%.

## Results

The auto-scaling mechanism works as expected. When the CPU usage goes beyond 75%, the Python script (provided in the codebase) successfully launches a new GCP instance. I confirmed the results through stress testing and monitoring via Prometheus.
