from pathlib import Path
from string import Template

def render_template(tpl_path: Path, mapping: dict, out_path: Path) -> None:
    tpl = Template(tpl_path.read_text(encoding="utf-8"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(tpl.safe_substitute(mapping), encoding="utf-8")

STRUCTURE = ["src", "tests", "docs", "src/app/__init__.py"]

def scaffold(base: Path, project: str) -> None:
    for rel in STRUCTURE:
        p = base / project / rel
        if rel.endswith(".py") or rel.endswith(".md"):
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(f"# {project}\n", encoding="utf-8")
        else:
            p.mkdir(parents=True, exist_ok=True)
