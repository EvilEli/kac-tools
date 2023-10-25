import re
from pathlib import PurePath
from collections import OrderedDict

RE_SECTION_PREFIX = r"## "
RE_SECTION_HEADER_PART = r"([^\[\]\s]+)"
RE_SECTION_CONTENT = r"([\s\S]+?)"
RE_ABSOLUTE_END_STRING = r"\Z"

RE_SECTION = f"{RE_SECTION_PREFIX}\[?{RE_SECTION_HEADER_PART} - {RE_SECTION_HEADER_PART}\]?.*${RE_SECTION_CONTENT}(?=(^{RE_SECTION_PREFIX})|({RE_ABSOLUTE_END_STRING}))"


class Section:
    def __init__(self, title: str, date: str, content: str):
        self.title = title
        self.date = date
        self.content = content

    def __repr__(self) -> str:
        return f"{self.title} - {self.date}\n{self.content}"


class Changelog:
    def __init__(self, path: PurePath):
        self.path = path
        self.content = self.read_content()
        self.sections = self.parse_sections()

    def __getitem__(self, title):
        if title == "latest":
            return next(iter(self.sections.values()))
        if title not in self.sections:
            return None
        return self.sections[title]

    def read_content(self):
        with open(self.path, "r") as f:
            content = f.read()
        return content

    def parse_sections(self):
        section_capture_list = re.findall(
            RE_SECTION,
            self.content,
            re.MULTILINE,
        )
        return OrderedDict(
            [
                (title, Section(title, date, content))
                for title, date, content, _, _ in section_capture_list
            ]
        )
