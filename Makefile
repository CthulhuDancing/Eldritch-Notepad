.PHONY: check

check:
	python -c "import ast, pathlib; [ast.parse(path.read_text(), filename=str(path)) for path in pathlib.Path('tests').rglob('*.py')]"
	python tests/test-marketplace.py
