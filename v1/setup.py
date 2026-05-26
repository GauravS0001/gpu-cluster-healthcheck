from setuptools import setup, find_packages


setup(
    name="gpu-cluster-healthcheck",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
        "kubernetes",
        "requests",
        "psutil"
    ],
    entry_points={
        "console_scripts": [
            "gpu-healthcheck=gpucheck.cli:cli"
        ]
    }
)