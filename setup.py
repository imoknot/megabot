import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "requests<=2.28.0",
    "pydantic==1.10.6"
]

setuptools.setup(
    name="megabot",
    version="0.0.1",
    author="Aleksandr Koksharov",
    author_email="koksharov@yandex.ru",
    description="A Hello World package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericjaychi/sample-pypi-package",
    packages=setuptools.find_packages(),
    # install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
