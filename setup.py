import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chambpy",
    version="0.0.1",
    author="Bryce Chamberlain",
    author_email="bryce@superchordate.com",
    description="My commonly used code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/superchordate/chambpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)