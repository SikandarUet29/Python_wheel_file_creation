import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt","r") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="custom_test_wheel",
    version="0.0.1",
    author="Sikandar Naseer",
    author_email="sikandarnaseer07@gmail.com",
    description="Package for creation custom wheel file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # packages=setuptools.find_packages(),   # use this line to automatically add the packages with __init_- file - use below line to custom add the packages
    packages=["calculator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Custom License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires = required

)