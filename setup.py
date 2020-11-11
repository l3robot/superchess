import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="superchess",
	version="0.0.1",
	author=["Samuel Laferriere", "Emile Robitaille"],
	author_email="samlaf92@gmail.com",
	description="A very basic chess platform",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/l3robot/superchess.git",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
