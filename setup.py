import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


requirements = [
    "requests",
    "pydantic"
]

setuptools.setup(
    name="megabot",
    version="0.0.4",
    author="Aleksandr Koksharov",
    author_email="koksharov@yandex.ru",
    description="Python telegram API adapter for FastAPI and asyncio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imoknot/megabot",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Pre-Alpha",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/imoknot/megabot/issues",
        "Changelog": "https://github.com/imoknot/megabot/blob/master/CHANGELOG.md",
    },
    python_requires='>=3.10',
)
