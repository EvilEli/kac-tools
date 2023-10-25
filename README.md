# kac-parser
`kac-parser` is a CLI python tool which parses CHANGELOG.md (in the keep-a-changelog format).
It can be used to extract only specific sections.

## Installation
### Release
The latest release is available in the public PyPi repo. 
Install via pip:
```
pip install kac-parser
```

### From git repo
You can also install directly from the git repo.

1. Clone the repository

```
git clone <git-url> <destination>
```

2. Change into the clone directory
```
cd <destination>
```

3. Install via pip
```
pip install .
```

## Usage
```
usage: kac-parser [-h] [-c CHANGELOG_FILE] [-s SECTION]

options:
  -h, --help            show this help message and exit
  -c CHANGELOG_FILE, --changelog-file CHANGELOG_FILE
                        Path to changelog file to parse (default: CHANGELOG.md).
  -s SECTION, --section SECTION
                        Section that should be extracted (default: latest).
```