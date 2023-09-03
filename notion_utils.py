from __future__ import annotations

import re
from datetime import datetime


def create_property(title: str, url: str, date: datetime, summary: str) -> dict:
    date = date.strftime("%Y-%m-%d")
    return {
        "title": {"title": [{"text": {"content": title}}]},
        "URL": {"url": url},
        "Date": {"date": {"start": date}},
        "summary": {"rich_text": [{"type": "text", "text": {"content": summary}}]},
    }


def create_header1(text: str) -> dict:
    return {
        "type": "heading_1",
        "heading_1": {"rich_text": [{"type": "text", "text": {"content": text}}]},
    }


def create_toggle(summary: str, detail: list[dict]) -> dict:
    return {
        "type": "toggle",
        "toggle": {
            "rich_text": [{"type": "text", "text": {"content": summary}}],
            "children": detail,
        },
    }


def create_paragraph(text: str, annotations: dict = {}):
    annotations_dict = {
        "bold": False,
        "italic": False,
        "strikethrough": False,
        "underline": False,
        "code": False,
        "color": "default",
    }
    annotations_dict.update(annotations)

    return {
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": text,
                    },
                    "annotations": annotations_dict,
                }
            ]
        },
    }


def create_linked_text(text: str, link: str):
    return {
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": text, "link": {"url": link}},
                    "href": link,
                }
            ]
        },
    }


def create_bullet_list(text: str):
    return {
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": text,
                    },
                }
            ]
        },
    }


def parse_output(output: str):
    blocks = []
    for line in output.split("\n"):
        line = line.strip()
        # line surrounded by ** **
        if re.match(r"^\*\*.*\*\*$", line):
            line = re.sub(r"^\*\*", "", line)
            line = re.sub(r"\*\*$", "", line)
            blocks.append({"object": "block", **create_paragraph(line, {"bold": True})})
        # line start with -
        elif re.match(r"^-", line):
            line = re.sub(r"^-", "", line).strip()
            blocks.append({"object": "block", **create_bullet_list(line)})
        else:
            blocks.append({"object": "block", **create_paragraph(line)})

    return blocks
