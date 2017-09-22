from setuptools import setup

setup(name="pyjamendo",
      version="0.0.1",
      author="Matthias Brandt",
      author_email = "the.matthias.brandt@gmail.com",
      description="A Python module to access the Jamendo API v3.0.",
      packages=['pyjamendo'],
      py_modules=["pyjamendo"],
      setup_requires=['requests'])