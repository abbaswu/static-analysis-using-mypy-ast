import sys
import logging
import typing

from mypy.build import build, BuildResult
from mypy.options import Options
from mypy.modulefinder import BuildSource
from mypy.traverser import TraverserVisitor
from mypy.types import TypeStrVisitor
from mypy.nodes import FuncDef, MypyFile, Node, Block, ClassDef
from mypy.errors import CompileError


def mypy_static_analysis(
    module_search_path: str,
    module_names_to_file_paths: typing.Mapping[str, str]
) -> BuildResult:
    """MUST BE USED ON MYPY 0.720 (PYTHON 3.7) OR BELOW.
    Build the AST and perform semantic analysis for a Python project.

    The tree for a module `module_name` (of type `mypy.nodes.MypyFile`) is accessible via:
    `result.graph[module_name].tree`
    where `result` (of type `mypy.build.BuildResult`) is the return value of this function."""
    options = Options()

    sources = [
        BuildSource(path=file_path, module=module_name, text=None, base_dir=module_search_path)
        for module_name, file_path in module_names_to_file_paths.items()
    ]
    
    result = build(sources=sources, options=options)

    return result
