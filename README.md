# Car Mechanic Simulator 2026 – Traditional Chinese (zh-Hant) localization

Contribution for the Red Dot Games dev team. Not an end-user installer.

## What this is

A complete Traditional Chinese (Taiwan) language file for the CMS 2026 Demo.
It started from the existing Simplified Chinese ALPHA file and was then reviewed and rewritten by hand against
`English.txt`, using natural Taiwan terminology instead of literal translation.

## Integration

- File: `Localizations/Traditional Chinese.txt` → `StreamingAssets/Localizations/`
- No code or font change was needed on the demo build: the game lists every `*.txt` in that folder, the menu label
  comes from the first line (`d=Traditional Chinese`), and no missing glyphs were observed.
- The menu order follows the file name. Renaming it to `English_Traditional Chinese.txt` lists it right after
  `English.txt` (verified on the demo build).

## Format guarantees (checked by `tools/check.py`)

- Same line count (11180), same keys and same order as `English.txt`; CRLF, UTF-8 without BOM.
- `{0}` `{1}` `<color=..>` `<size=..>` `<sprite ..>` `\n` and `|` (line-break separator) match the English line.
- `^!key suffix` / `^SeatName suffix` = reference to another key's text + suffix. The suffix is usually a car or seat
  **model name** (proper noun) and is kept in English; only descriptive words (Leather, Fabric, Wall, Stage, …)
  are translated.
- Engine codes (e.g. `V10 VENM1070`) and unused `^!xxx` placeholders are untouched.

## Translation rules

- Taiwan terminology, written for ordinary players (not only mechanics). "Order" stays "訂單".
- Part names are generated from one root dictionary (`tools/parts_dict.txt`) so a part has one name everywhere.
- Car, seat, brand and engine-code names stay in English.

## Repository layout

| Path | Purpose |
|---|---|
| `Localizations/Traditional Chinese.txt` | The language file |
| `tools/parts_dict.txt` | Part root-word dictionary (`EN=>ZH`); rerun `apply_parts.py` after editing |
| `tools/glossary.tsv` | Terminology replacements used after the initial conversion |
| `patches/*.txt` | Manual review log, one `line|new text` per row; re-appliable |
| `tools/apply_patches.py` | Applies patches and rejects any line whose tags / `\|` differ from English |
| `tools/check.py` | Line count, key and tag parity check |
| `tools/pair.py a b` | Prints English and Chinese side by side for lines a–b (review aid) |
| `tools/fix_refs.py` | Restores model names in `^` reference lines |

The scripts expect `Traditional Chinese.txt` in the working directory and read `English.txt` from the path in the
`D =` constant at the top of each script – change it to your path. Use `set PYTHONUTF8=1` on Windows consoles.

## Adding another language the same way

1. Copy `English.txt` to `<Name>.txt`; set line 1 to `d=<menu label>`.
2. Translate only the text after the first `=`; keep keys, line count and tags.
3. Run `py tools/check.py`; no `KEY` / `TAG` output means it passes.

## Notes and limitations

- Based on the demo build; strings added in the full release will need translating.
- No native-speaker proofreading pass yet. Corrections are welcome as additional files in `patches/`.
