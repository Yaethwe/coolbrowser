import subprocess

def install_packages(package_list):
    for package in package_list:
        subprocess.check_call(["pip", "install", package])

# Example: List of packages to install
packages_to_install = ['emoji', 'PyQt5', 'PyQtWebEngine', 'PyQt5.QtWebKitWidgets']
infom = """
Install packages may take a few minutes.
"""
print(infom)
# Install the packages
install_packages(packages_to_install)