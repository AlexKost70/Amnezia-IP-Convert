# Amnezia IP List Converter

Russian version: [README.md](README.md)

A simple script that converts JSON/IP range lists into `ip-list.json` format for Amnezia.

## What it does

Transforms input data into an array of objects like:

```json
[
    {
        "hostname": "1.2.3.0/24",
        "ip": ""
    }
]
```

## Supported input formats

- plain text file with one IP/CIDR range per line;
- JSON array of strings:
  - `["1.2.3.0/24", "5.6.7.0/24"]`;
- JSON array of objects with the `hostname` field:
  - `[{"hostname":"1.2.3.0/24"}]`.

## Requirements

- Python 3.9+.

## Installation

Install locally from the project directory:

```bash
python -m pip install .
```

Install in editable (development) mode:

```bash
python -m pip install -e .
```

Install directly from GitHub:

```bash
python -m pip install "git+https://github.com/<user>/<repo>.git"
```

## Usage

Without installation (run script directly):

```bash
python amnezia-ip-convert.py input.json output-ip-list.json
```

After installation (via CLI command):

```bash
amnezia-ip-convert input.json output-ip-list.json
```

Where:
- `input.json` is your source file with IP addresses/CIDR ranges;
- `output-ip-list.json` is the generated file in Amnezia JSON format.

## Project structure

- `amnezia-ip-convert.py` - run without installation;
- `amnezia_ip_convert.py` - main converter module;
- `README.md` - Russian documentation;
- `README.en.md` - English documentation;
- `.gitignore` - Git ignore rules;
- `LICENSE` - MIT license.

