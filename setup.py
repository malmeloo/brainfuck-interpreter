import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brainfuck-interpreter",
    version="1.0.0",
    author="Mike A.",
    author_email="dismissed.is.a.guy@gmail.com",
    description="An object-oriented highly flexible brainfuck interpreter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DismissedGuy/brainfuck-interpreter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters"
    ],
    python_requires='>=3.6',
)
