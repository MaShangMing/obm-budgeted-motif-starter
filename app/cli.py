"""JSON file adapter for the placement solver."""
import json
from pathlib import Path
import sys
from solver import solve

def main():
    if len(sys.argv) != 3:
        print('usage: cli.py INPUT_JSON OUTPUT_JSON', file=sys.stderr)
        return 2
    try:
        raw = Path(sys.argv[1]).read_text(encoding='utf-8')
        result = solve(json.loads(raw))
    except (ValueError, TypeError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False)+'\n', encoding='utf-8')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
