from setuptools import setup, find_packages

setup(
    name="heart_disease_api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "pydantic",
        "uvicorn",
        "pandas",
        "joblib",
        "scikit-learn",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "heart_disease_api = fastapi_skeleton.main:app",
        ],
    },
)
