
from pprint import pprint

project = {
    "name": "IT Knowledge Base",
    "authors": ["Tim", "Anna"],
    "modules": {
        "python": {"lessons": 122, "status": "ready"},
        "devops": {"lessons": 85, "status": "draft"}
    },
    "tags": ["education", "docs", "backend"]
}

pprint(project, width=60, sort_dicts=False)
