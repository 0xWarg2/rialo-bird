from setuptools import setup, find_packages

setup(
    name="rialo-bird",
    version="0.1.0",
    description="A Flappy Bird clone built with Python Arcade for web browsers",
    author="Rialo Bird Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "arcade>=2.6.17",
        "pygbag>=0.6.0",
        "httpx>=0.28.1",
        "python-dotenv>=1.1.1",
    ],
    extras_require={
        "dev": [
            "black>=24.10.0",
            "flake8>=7.1.1",
            "pytest>=8.3.4",
            "pytest-asyncio>=0.24.0",
            "playwright>=1.48.0",
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

