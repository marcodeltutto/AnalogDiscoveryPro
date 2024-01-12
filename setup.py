from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
   name = "ADP_API",
   version = "1.0",
   description = "This module realizes communication with Digilent Test & Measurement devices",
   license = "MIT",
   long_description = long_description,
   author = "Marco Del Tutto",
   author_email = "marco.deltutto@gmail.com",
   packages = ["ADP_API"],
)
