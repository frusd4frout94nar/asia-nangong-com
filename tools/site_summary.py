import json
import sys
from datetime import datetime
from pathlib import Path


SITE_DATA = [
    {
        "name": "asia-nangong",
        "url": "https://asia-nangong.com",
        "keywords": ["南宫体育", "体育资讯", "赛事数据", "运动社区"],
        "tags": ["体育", "资讯", "社区"],
        "description": "一个专注体育赛事与运动社区的平台，提供最新赛事数据、热门体育资讯和用户互动空间。"
    }
]


def generate_summary(entry: dict) -> str:
    lines = []
    lines.append(f"站点名称: {entry['name']}")
    lines.append(f"URL: {entry['url']}")
    lines.append(f"关键词: {'、'.join(entry['keywords'])}")
    lines.append(f"标签: {'、'.join(entry['tags'])}")
    lines.append(f"简短说明: {entry['description']}")
    lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(lines)


def to_markdown(entry: dict) -> str:
    md_lines = []
    md_lines.append(f"# {entry['name']}")
    md_lines.append("")
    md_lines.append(f"- **URL**: [{entry['url']}]({entry['url']})")
    keywords_str = ", ".join(entry['keywords'])
    md_lines.append(f"- **关键词**: {keywords_str}")
    tags_str = ", ".join(entry['tags'])
    md_lines.append(f"- **标签**: {tags_str}")
    md_lines.append(f"- **简短说明**: {entry['description']}")
    md_lines.append("")
    md_lines.append(f"_摘要生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")
    return "\n".join(md_lines)


def to_json(entry: dict) -> str:
    output = {
        "name": entry['name'],
        "url": entry['url'],
        "keywords": entry['keywords'],
        "tags": entry['tags'],
        "description": entry['description'],
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(output, ensure_ascii=False, indent=2)


def print_summary(entry: dict, fmt: str = "text") -> None:
    if fmt == "text":
        print(generate_summary(entry))
    elif fmt == "markdown":
        print(to_markdown(entry))
    elif fmt == "json":
        print(to_json(entry))
    else:
        print(f"不支持的格式: {fmt}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    format_choice = "text"
    if len(sys.argv) > 1:
        format_choice = sys.argv[1].lower()
    if format_choice not in ("text", "markdown", "json"):
        print(f"用法: python tools/site_summary.py [text|markdown|json]", file=sys.stderr)
        sys.exit(1)

    for site in SITE_DATA:
        print_summary(site, fmt=format_choice)
        if len(SITE_DATA) > 1:
            print("\n" + "=" * 40 + "\n")


if __name__ == "__main__":
    main()