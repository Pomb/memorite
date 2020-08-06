import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="memorite-pkg-paullombard",
    version="0.0.1",
    author="Paul Lombard",
    author_email="pmlomb.memorite@gmail.com",
    description="A console app to aid memorizing text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pomb/memorite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
