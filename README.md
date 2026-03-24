# Tweet Idol Generator

インバウンド向けのアイドル系デリヘルアカウント用に、**健全な内容**のSNS投稿案を生成するCLIツールです。

- 英語（EN）
- 台湾向け繁体字中国語（ZH-TW）

> ※内容はアイドル文化紹介や「かわいい」表現に寄せた、安心なテキストのみです。

## 使い方

```bash
python3 tweet_generator.py --theme kawaii --count 5
```

### オプション

- `--theme`: 投稿テーマ
  - `idol-culture`
  - `kawaii`
  - `omotenashi`
  - `city-walk`
  - `fan-love`
- `--count`: 生成する投稿ペア数（英語＋繁体字）
- `--seed`: 乱数シード（再現性が必要なとき）

## 実行例

```bash
python3 tweet_generator.py --theme idol-culture --count 2 --seed 42
```

出力例:

```text
# Inbound Idol Account Post Generator
Theme: idol-culture

## Post 1
EN: Welcome to Japan's Japanese idol culture! ✨ Today we're celebrating smiles, style, and sweet energy. #Kawaii #JapanTrip
ZH-TW: 歡迎來感受日本偶像文化的魅力！✨ 今天一起分享笑容、時尚和甜甜能量。#可愛 #日本旅行
```
