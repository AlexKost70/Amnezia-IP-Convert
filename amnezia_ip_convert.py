#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_source_entries(input_path: Path) -> list[str]:
    text = input_path.read_text(encoding="utf-8").strip()
    if not text:
        return []

    # Try parsing as JSON first; fallback to plain text lines.
    try:
        data = json.loads(text)
        if isinstance(data, list):
            result = []
            for item in data:
                if isinstance(item, str):
                    value = item.strip()
                    if value:
                        result.append(value)
                elif isinstance(item, dict):
                    value = str(item.get("hostname", "")).strip()
                    if value:
                        result.append(value)
            return result
    except json.JSONDecodeError:
        pass

    return [line.strip() for line in text.splitlines() if line.strip()]


def convert_entries(entries: list[str]) -> list[dict[str, str]]:
    return [{"hostname": entry, "ip": ""} for entry in entries]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert IP JSON into Amnezia-compatible ip-list JSON format."
    )
    parser.add_argument("input", help="Path to source file with IP ranges")
    parser.add_argument(
        "output",
        help="Path to output file in Amnezia ip-list JSON format (e.g. ip-list.json)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    entries = load_source_entries(input_path)
    transformed = convert_entries(entries)

    output_path.write_text(
        json.dumps(transformed, ensure_ascii=False, indent=4) + "\n",
        encoding="utf-8",
    )

    print(f"Converted {len(transformed)} entries -> {output_path}")


if __name__ == "__main__":
    main()
