from setuptools import setup, find_packages

setup(
    name="headless_setup",
    version="0.1",
    packages=find_packages(),
    author="retrodaredevil",
    author_email="retrodaredevil@gmail.com",
    description="Easily setup your Raspberry Pi without a monitor or keyboard",
    url="https://github.com/retrodaredevil/headless-setup",
    entry_points={"console_scripts": ["headless-setup = headless_setup:main"]}
)
