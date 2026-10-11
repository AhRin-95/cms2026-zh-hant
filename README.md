# Car Mechanic Simulator 2026 — 繁體中文（Traditional Chinese）語言檔

## For the dev team (English summary)

Drop-in localization: copy `Localizations/Traditional Chinese.txt` into
`StreamingAssets/Localizations/`. The game lists every `*.txt` in that folder; the display name comes from the
first line (`d=Traditional Chinese`). The menu order follows the file name: rename it to
`English_Traditional Chinese.txt` if you want it listed right after `English.txt` (verified on the demo build).
No code change, no font change needed (no missing glyphs on the demo build).

Format notes (must keep, `tools/check.py` verifies them):
- Same line count and same keys as `English.txt` (11180 lines, CRLF, UTF-8 **without** BOM).
- `{0}`, `{1}`, `<color=..>`, `<size=..>`, `<sprite ..>`, `\n` and `|` (line break) must match the English line.
- `^!key suffix` / `^SeatName suffix` = reference to another key's text + suffix. The suffix is usually a car or
  seat **model name** (proper noun) → keep English; only translate descriptive words (Leather, Fabric, Wall, Stage…).
- Engine codes like `V10 VENM1070` and `^!xxx` placeholders stay untouched.

## 安裝（玩家／測試者）

1. 把 `Localizations/Traditional Chinese.txt` 複製到
   `Car Mechanic Simulator 2026 Demo_Data/StreamingAssets/Localizations/`
2. 遊戲內：設定 → 語言 → `Traditional Chinese`。
   （選單順序依檔名排序；想讓它排在 English 後面，把檔名改成 `English_Traditional Chinese.txt`。）

## 翻譯原則

- 用台灣玩家與修車現場的說法，不照字面直譯（例：Piemenu→輪盤選單、Junkyard→廢車場、Dyno→動力計、Servo→加力器、
  Coolant reservoir→副水箱、Rocker cover→汽門室蓋）。
- 讓一般玩家看得懂，不要變成只有修車人員才懂的版本（Order 維持「訂單」）。
- 車款、座椅、品牌、引擎型號一律保留英文。
- 同一零件全檔譯名一致：零件名由 `tools/parts_dict.txt`（詞根字典）統一產生。

## 目錄

| 路徑 | 用途 |
|---|---|
| `Localizations/Traditional Chinese.txt` | 成品，直接使用 |
| `tools/parts_dict.txt` | 零件詞根字典（英文=>中文），改這裡再跑 `apply_parts.py` |
| `tools/glossary.tsv` | 簡轉繁後的用語置換表 |
| `patches/*.txt` | 人工校對紀錄，格式 `行號\|新譯文`，可重複套用 |
| `tools/apply_patches.py` | 套用 patches，並檢查標籤／`\|` 是否與英文一致 |
| `tools/check.py` | 行數、key、標籤檢查 |
| `tools/pair.py a b` | 並列顯示第 a–b 行的英文與中文，方便審稿 |

## 新增或更新語言（給 dev team 的通用步驟）

1. 複製 `English.txt`，改名為 `<排序用前綴>_<語言>.txt`（要排在哪個語言後面，就用那個語言名開頭＋`_`）。
2. 第一行改成 `d=<選單顯示的名稱>`。
3. 逐行翻譯 `=` 後面的文字；不要動 key、行數與標籤。
4. 執行 `py tools/check.py`（需放在含 `Traditional Chinese.txt` 的目錄；路徑見腳本內 `D=`），沒有輸出 KEY／TAG 即通過。
5. 放進 `StreamingAssets/Localizations/`，遊戲內語言選單即會出現。

## 修改流程（本語言）

```
py tools/apply_parts.py        # 只在改了 parts_dict.txt 時
py tools/apply_patches.py patches/NNN.txt
py tools/fix_refs.py           # 還原 ^ 引用行的型號名
py tools/check.py
```

> 注意：腳本內英文檔路徑 `D=` 寫的是作者機器的遊戲路徑，請改成你的 `English.txt` 位置。
> 若 Windows 主控台出現編碼錯誤，先執行 `set PYTHONUTF8=1`。

## 已知限制

- 目前以 Demo 版內容翻譯，完整版新增字串需再補。
- 尚未有母語審稿者全面校閱；歡迎在 `patches/` 追加修正。
