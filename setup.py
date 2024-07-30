import setuptools

with open("README.md","r",encoding="utf-8")as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME= "End-to-end-ML-Project-Implimentation"
AUTHER_USER_NAME="SHIRISH"
SRC_REPO="wine quality project"
AUTHER_EMAIL= "utageshirish@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    auther=AUTHER_USER_NAME,
    auther_email= AUTHER_EMAIL,
    description = "A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https"

)