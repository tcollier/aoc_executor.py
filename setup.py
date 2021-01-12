import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aoc-executor",
    version="0.0.3",
    author="Tom Collier",
    author_email="tcollier@gmail.com",
    description="Python executor for AoC solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tcollier/aoc_executor.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
