import os
import sys
import shutil
import subprocess
import zipfile

class DependencyInstaller:
    def __init__(self, base_path):
        self.base_path = base_path
        self.vendor_path = os.path.join(self.base_path, "..", "vendor") # Adjusted for PyInstaller
        self.install_path = os.path.join(self.base_path, "installed_dependencies")
        os.makedirs(self.install_path, exist_ok=True)

    def install_node(self):
        print("Installing Node.js...")
        node_archive = os.path.join(self.vendor_path, "node-v20.11.0-linux-x64.zip") # Placeholder name
        node_install_dir = os.path.join(self.install_path, "node")

        if not os.path.exists(node_archive):
            print(f"Error: Node.js archive not found at {node_archive}")
            return

        os.makedirs(node_install_dir, exist_ok=True)
        with zipfile.ZipFile(node_archive, 'r') as zip_ref:
            zip_ref.extractall(node_install_dir)
        print("Node.js installed.")

    def install_android_sdk(self):
        print("Installing Android SDK...")
        android_sdk_archive = os.path.join(self.vendor_path, "android-sdk-linux.zip") # Placeholder name
        android_sdk_install_dir = os.path.join(self.install_path, "android-sdk")

        if not os.path.exists(android_sdk_archive):
            print(f"Error: Android SDK archive not found at {android_sdk_archive}")
            return

        os.makedirs(android_sdk_install_dir, exist_ok=True)
        with zipfile.ZipFile(android_sdk_archive, 'r') as zip_ref:
            zip_ref.extractall(android_sdk_install_dir)
        print("Android SDK installed.")

    def _run_npm_command(self, args, cwd=None):
        node_bin = os.path.join(self.install_path, "node", "bin", "node")
        npm_cli = os.path.join(self.install_path, "node", "lib", "node_modules", "npm", "bin", "npm-cli.js")

        if not os.path.exists(node_bin):
            print(f"Error: Node.js executable not found at {node_bin}")
            return False
        if not os.path.exists(npm_cli):
            print(f"Error: npm CLI not found at {npm_cli}")
            return False

        command = [node_bin, npm_cli] + args
        print(f"Running npm command: {' '.join(command)}")
        try:
            process = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=True)
            print(process.stdout)
            if process.stderr:
                print(process.stderr)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error running npm command: {e}")
            print(f"Stdout: {e.stdout}")
            print(f"Stderr: {e.stderr}")
            return False

    def install_appium_server(self):
        print("Installing Appium Server...")
        # Ensure npm is installed with the bundled node
        if not self._run_npm_command(["install", "-g", "npm@latest", "--prefix", os.path.join(self.install_path, "node")]):
            print("Failed to update npm.")
            return

        if self._run_npm_command(["install", "-g", "appium@latest", "--prefix", self.install_path]):
            print("Appium Server installed.")
        else:
            print("Failed to install Appium Server.")

    def install_appium_drivers(self):
        print("Installing Appium Drivers...")
        appium_bin = os.path.join(self.install_path, "bin", "appium")
        if not os.path.exists(appium_bin):
            print(f"Error: Appium executable not found at {appium_bin}. Cannot install drivers.")
            return

        # Install xcuitest-driver
        if self._run_npm_command(["exec", appium_bin, "driver", "install", "xcuitest"], cwd=self.install_path):
            print("xcuitest-driver installed.")
        else:
            print("Failed to install xcuitest-driver.")

        # Install uiautomator2-driver
        if self._run_npm_command(["exec", appium_bin, "driver", "install", "uiautomator2"], cwd=self.install_path):
            print("uiautomator2-driver installed.")
        else:
            print("Failed to install uiautomator2-driver.")

    def install_all(self):
        print("Starting Mobile Agent installation...")
        self.install_node()
        self.install_android_sdk()
        self.install_appium_server()
        self.install_appium_drivers()
        print("Mobile Agent installation complete.")
