from pathlib import PurePath
from collections import OrderedDict


class Section:
    def __init__(self, title: str, date: str, content: str):
        self.title = title
        self.date = date
        self.content = content

    def __repr__(self) -> str:
        if self.date:
            return f"{self.title} - {self.date}\n{self.content}"
        return f"{self.title}\n{self.content}"


class Changelog:
    def __init__(self, path: PurePath):
        self.path = path
        self.content = self.read_content()
        self.sections = self.parse_sections()

    def __getitem__(self, title):
        if title == "latest":
            return next(x for x in self.sections.values() if x.title != "Unreleased")

        if title not in self.sections:
            return None

        return self.sections[title]

    def read_content(self):
        with open(self.path, "r") as f:
            content = f.read()
        return content

    def parse_sections(self):
        section_dict = OrderedDict()
        section_list = self.content.split("\n## ")
        for sec in section_list[1:]:
            title, content = sec.split("\n", 1)
            if " - " in title:
                title, date = title.split(" - ")
            else:
                date = None
            section_dict[title] = Section(title, date, content)
        return section_dict
