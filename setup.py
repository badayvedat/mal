from setuptools import setup, find_packages
import os
import sys
import sysconfig

# Ship tet.pth into site-packages so `site` auto-executes it on interpreter startup.
# Wheel data_files are installed relative to sys.prefix, so an absolute site-packages
# path gets re-rooted (nested under site-packages) and never scanned. Use the path
# relative to sys.prefix so the file lands directly in site-packages.
site_packages = os.path.relpath(sysconfig.get_paths()["purelib"], sys.prefix)

setup(
    name="tet",
    version="0.1.0",
    description="Add your description here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    url="",
    packages=find_packages(),
    data_files=[(site_packages, ["tet.pth"])],
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
