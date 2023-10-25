"""Contains tests for MotionHandler class"""
import pytest
import os
from keepachangelog_tools.changelog import Changelog
from pathlib import PurePath

@pytest.fixture()
def test_changelog_file():
    test_changelog_file = PurePath("test_changelog.md")
    with open(test_changelog_file, "w") as file:
        content = [
            "# Changelog\n",
            "## Unreleased\n",
            "## v1.0.1\n"
            "## v1.0.0\n"
            "## v0.1.1\n"
            "### Fixed\n"
            "- [Patch] Added bugfix.\n"
            "## v0.1.0\n"
            "- [Minor] Initial release\n"
        ]
        file.writelines(content)

    yield test_changelog_file
    os.remove(test_changelog_file)

class TestChangelog:
    def test_changelog_init(self, test_changelog_file):
        changelog = Changelog(test_changelog_file)

    def test_changelog_titles(self, test_changelog_file):
        changelog = Changelog(test_changelog_file)
        titles = [sec.title for sec in changelog.sections.values()]
        assert titles == ["Unreleased", "v1.0.1", "v1.0.0", "v0.1.1", "v0.1.0"]

