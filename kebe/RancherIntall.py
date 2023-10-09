import subprocess

def install_rancher():
    try:
        # Rancher를 설치하기 위한 Docker 커맨드
        command = ["docker", "run", "-d", "--restart=unless-stopped", "-p", "80:80", "-p", "443:443", "--privileged", "rancher/rancher:latest"]

        # 커맨드 실행
        subprocess.run(command, check=True)
        print("Rancher has been installed successfully.")

    except subprocess.CalledProcessError:
        print("Error during the installation of Rancher.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    install_rancher()