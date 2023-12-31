import os
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

requirements_path = here / "requirements" / "base.txt"
redis_requirements_path = here / "requirements" / "redis.txt"

long_description = (here / "README.md").read_text()


def read_requirements(path: Path) -> list[str]:
    """Read requirements from a file."""
    try:
        with path.open(mode="rt", encoding="utf-8") as fp:
            return list(filter(None, (line.split("#")[0].strip() for line in fp)))
    except IndexError as err:
        raise RuntimeError(f"Could not read file: {path}") from err


setup(
    name="camora",
    description="Lightweight task scheduler",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    version=os.getenv("PACKAGE_VERSION", "0.0.0"),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7.0",
    extras_require={"redis": read_requirements(redis_requirements_path)},
    install_requires=read_requirements(requirements_path),
    author="Piotr Tobiasz",
    author_email="piotr.tobiasz.dev@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
