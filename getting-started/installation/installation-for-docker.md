# 🐋 Installation for Docker

## Installing Docker for Windows/Mac

{% hint style="warning" %}
For Windows and Mac (x86_64/arm64) we recommend installing Docker Desktop. Especially Mac, as installation tends to be flaky via other means.
{% endhint %}

Download Docker Desktop:
https://www.docker.com/products/docker-desktop/

{% hint style="info" %}
Requires Windows 10/11 Pro, Enterprise, or Education and CPU virtualization enabled in BIOS (Intel VT-x / AMD-V)
{% endhint %}

After installation, the Docker Desktop process needs to be running and can be backgrounded

## Installing Docker for Unix

{% hint style="success" %}
Docker can be installed on WSL2, as this version does not treat Docker as a nested hypervisor
{% endhint %}

## Installing Docker for Ubuntu/Debian

```bash
apt install docker.io
systemctl start docker
systemctl enable docker
```

## Installing Docker for Arch Linux

```bash
pacman -S docker
systemctl start docker
systemctl enable docker
```

{% hint style="info" %}
To avoid running Docker as root, without `sudo`

```bash
usermod -aG docker $USER
```

{% endhint %}

## Building NetExec Docker Container

Building and running the container

```bash
git clone https://github.com/Pennyw0rth/NetExec
cd NetExec
docker build -t netexec .
docker run --rm -it netexec --help
```
