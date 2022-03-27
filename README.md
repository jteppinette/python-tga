# Python TGA

_A Python package which supports working with TGA, also known as TARGA
(Truevision Advanced Raster Graphics Adapter), files._

## Features

**Specification**

This library only currently supports creating and exporting images of
the following image types:

- Uncompressed RGB/A 24/32 Bit Depth

**Python**

- Type Hints / Editor Completion
- Readable
- Fully Tested
- Python 3.6 - 3.10 Support

## Install

```sh
$ pip install tga
```

## Usage

```python
import tga

black = tga.Color(0, 0, 0)

image = tga.Image(500, 500)
image.set_pixel(0, 0, 0, black)

with open("image.tga", "wb") as file:
	file.write(image.to_bytes())
```

## Development

### Required Software

Refer to the links provided below to install these development dependencies:

- [direnv](https://direnv.net)
- [git](https://git-scm.com/)
- [pyenv](https://github.com/pyenv/pyenv#installation)

### Getting Started

**Setup**

```sh
$ <runtimes.txt xargs -n 1 pyenv install -s
$ direnv allow
$ pip install -r requirements/dev.txt
$ pre-commit install
$ pip install -e .
```

**Tests**

_Run the test suite against the active python environment._

```sh
$ pytest
```

_Run the test suite against the active python environment and watch the codebase
for any changes._

```sh
$ ptw
```

_Run the test suite against all supported python versions._

```sh
$ tox
```

### Publishing

**Create**

1. Update the version number in `tga/__init__.py`.

2. Add an entry in `HISTORY.md`.

3. Commit the changes, tag the commit, and push the tags:

   ```sh
   $ git commit -am "v<major>.<minor>.<patch>"
   $ git tag v<major>.<minor>.<patch>
   $ git push --tags
   ```

4. Convert the tag to a release in GitHub with the history entry as the
   description.

**Build**

```sh
$ python -m build
```

**Upload**

```
$ twine upload dist/*
```
