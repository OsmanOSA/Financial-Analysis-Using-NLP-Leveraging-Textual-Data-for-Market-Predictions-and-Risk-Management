
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"


REPONAME = "FINANCIAL-ANALYSIS-USING-NLP-LEVERAGING-TEXTUAL-DATA-FOR-MARKET-PREDICTION-AND-RISK-MANAGEMENT"
AUTHOR = "OsmanOSA"
SRC_REPO = "Financial_Analysis"
AUTHOR_EMAIL = "saidaliosman12@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Financial Analysis using NLP: Leveraging textual data for market prediction and risk management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https//github.com/{AUTHOR}/{REPONAME}",
    projects_urls={
        "Bug Tracker": f"https//github.com/{AUTHOR}/{REPONAME}/issues",
},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)