from setuptools import setup, find_packages

setup(
    name="krbrelayx",
    version="1.0.0",
    description="Kerberos relay attack toolset",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    install_requires=[
        "setuptools>=61.0",
        "impacket>=0.9.22,<0.11.0",
        "ldap3>=2.9",
        "dnspython>=2.0"
    ],
    entry_points={
        "console_scripts": [
            # lets you call `krbrelayx` from the CLI if you have a main script
            "krbrelayx=krbrelayx.krbrelayx:main",
        ],
    },
    python_requires=">=3.8",
)
