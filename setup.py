from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="squidle_scivision",
    version="0.0.1",
    description="scivision plugin, using Squidle dataset",
    url="https://github.com/miquelmassot/squidle_scivision",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
    entry_points={
        "intake.drivers": ["squidle_csv = squidle_scivision.csv:SquidleCSVSource"]
    },
)
