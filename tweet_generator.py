#!/usr/bin/env python3
"""Generate wholesome inbound social posts for an idol-style delivery service account.

Outputs posts in:
- English
- Traditional Chinese (Taiwan)
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class PostTheme:
    key: str
    en: str
    zh_tw: str


THEMES: tuple[PostTheme, ...] = (
    PostTheme("idol-culture", "Japanese idol culture", "日本偶像文化"),
    PostTheme("kawaii", "kawaii moments", "可愛瞬間"),
    PostTheme("omotenashi", "warm hospitality", "貼心款待"),
    PostTheme("city-walk", "city adventure vibes", "城市散步氛圍"),
    PostTheme("fan-love", "fan appreciation", "粉絲感謝"),
)

EN_TEMPLATES: tuple[str, ...] = (
    "Welcome to Japan's {theme_en}! ✨ Today we're celebrating smiles, style, and sweet energy. #Kawaii #JapanTrip",
    "Looking for {theme_en} during your visit? We're sharing soft, cheerful vibes all day long 💖 #IdolCulture #TokyoLife",
    "A little sparkle for your timeline: {theme_en} + happy memories + adorable charm 🌸 #CuteJapan #Travel",
    "Today's mood: {theme_en}, pastel dreams, and kind hearts 🎀 #KawaiiMood #VisitJapan",
)

ZH_TW_TEMPLATES: tuple[str, ...] = (
    "歡迎來感受{theme_zh}的魅力！✨ 今天一起分享笑容、時尚和甜甜能量。#可愛 #日本旅行",
    "來日本想體驗{theme_zh}嗎？我們整天都在傳遞溫柔又療癒的氣氛 💖 #偶像文化 #東京生活",
    "給你一點閃亮靈感：{theme_zh}＋美好回憶＋超可愛氛圍 🌸 #可愛日本 #旅遊",
    "今日關鍵字：{theme_zh}、粉彩夢想和暖心感受 🎀 #可愛心情 #來日本玩",
)


def build_posts(theme: PostTheme, count: int, seed: int | None) -> list[dict[str, str]]:
    rng = random.Random(seed)
    posts: list[dict[str, str]] = []

    for _ in range(count):
        en = rng.choice(EN_TEMPLATES).format(theme_en=theme.en)
        zh_tw = rng.choice(ZH_TW_TEMPLATES).format(theme_zh=theme.zh_tw)
        posts.append({"en": en, "zh_tw": zh_tw})

    return posts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate wholesome English and Traditional Chinese (Taiwan) social posts."
    )
    parser.add_argument(
        "--theme",
        choices=[t.key for t in THEMES],
        default="kawaii",
        help="Post theme.",
    )
    parser.add_argument("--count", type=int, default=5, help="Number of post pairs to generate.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.count < 1:
        raise SystemExit("--count must be 1 or greater")

    theme = next(t for t in THEMES if t.key == args.theme)
    posts = build_posts(theme=theme, count=args.count, seed=args.seed)

    print("# Inbound Idol Account Post Generator")
    print(f"Theme: {theme.key}\n")

    for i, post in enumerate(posts, start=1):
        print(f"## Post {i}")
        print(f"EN: {post['en']}")
        print(f"ZH-TW: {post['zh_tw']}\n")


if __name__ == "__main__":
    main()
