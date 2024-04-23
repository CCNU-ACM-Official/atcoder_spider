

class problem:
    index = ""
    id = ""
    url = ""
    statement = ""
    samples = ""
    def __str__(self) -> str:
        return f"""
{self.index} {self.id} {self.url} {self.statement}
"""


class contest:
    id = ""
    contest_url = ""
    problems_addrs = []
    index = []
    name = []
    problems = []
    def __str__(self) -> str:
        return f"""{self.id} {self.contest_url}
{self.name}
"""

