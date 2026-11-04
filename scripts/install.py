#!/usr/bin/env python3
"""Install this checkout's skill bundle into a project's skill directory."""
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
LICENSE = ROOT / "licenses/mattpocock-skills-MIT.txt"


def install(target, check_only):
    target = target.expanduser().resolve()
    if target == SOURCE or SOURCE in target.parents or target in SOURCE.parents:
        raise ValueError("请选择业务项目的技能目录，安装目标与技能源码重叠。")

    files = {p.relative_to(SOURCE): p for p in sorted(SOURCE.rglob("*"))
             if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts}
    skill_count = sum(p.name == "SKILL.md" and len(p.parts) == 2 for p in files)
    if not skill_count or not LICENSE.is_file():
        raise ValueError("请从完整的技能库运行，缺少技能或上游许可文件。")
    files[Path("_shared") / LICENSE.name] = LICENSE

    missing = []
    conflicts = []
    for rel, source in files.items():
        dest = target / rel
        if dest.resolve() != dest or (dest.exists() and not dest.is_file()):
            conflicts.append(str(rel))
        elif dest.is_file():
            if dest.read_bytes() != source.read_bytes():
                conflicts.append(str(rel))
        elif any(parent.exists() and not parent.is_dir() for parent in dest.parents):
            conflicts.append(str(rel))
        else:
            missing.append(rel)
    if conflicts:
        raise ValueError("以下路径已有不同内容或链接。请先比较并合并或备份移出：\n" + "\n".join(conflicts))
    if check_only and missing:
        raise ValueError("安装目录缺少以下文件：\n" + "\n".join(map(str, missing)))

    for rel in missing:
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        with files[rel].open("rb") as source:
            output = dest.open("xb")
            try:
                with output:
                    shutil.copyfileobj(source, output)
                shutil.copymode(files[rel], dest)
            except (OSError, KeyboardInterrupt):
                dest.unlink()
                raise

    print(f"{skill_count} 项技能，{len(files)} 个文件（含共享参考和许可）")
    print(f"目标目录：{target}")
    if check_only:
        print("全部文件均与当前技能库一致。")
    else:
        print(f"新增 {len(missing)} 个文件。请在 Agent 中打开目标项目。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="把整套技能安装到指定目录，保留已有文件。")
    parser.add_argument("target", type=Path, help="Agent 从中发现各个技能的目录")
    parser.add_argument("--check", action="store_true", help="仅核对已安装文件与当前源码")
    args = parser.parse_args()
    try:
        install(args.target, args.check)
    except (OSError, ValueError) as error:
        sys.exit(str(error))
