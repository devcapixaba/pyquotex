"""The python wrapper for IQ Option API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="pyquotex",
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "appdirs==1.4.4",
        "beautifulsoup4==4.11.2",
        "certifi==2022.12.7",
        "charset-normalizer==3.1.0",
        "cloudscraper==1.2.69",
        "greenlet==2.0.1",
        "idna==3.4",
        "importlib-metadata==6.2.0",
        "playwright==1.32.1",
        "pyee==9.0.4",
        "pyparsing==3.0.9",
        "requests==2.28.2",
        "requests-toolbelt==0.10.1",
        "simplejson==3.18.3",
        "soupsieve==2.4",
        "tqdm==4.65.0",
        "typing_extensions==4.5.0",
        "urllib3==1.26.14",
        "websocket-client==1.3.3",
        "websockets==10.4",
        "zipp==3.15.0"
    ],
    include_package_data=True,
)