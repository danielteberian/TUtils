import os
import pathlib

PIPE = "|"
ELBOW = "|__"
TEE = "|--"
PIPE_PREFIX = "|  "
SPACE_PREFIX = "   "

class dirTree:
	def __init__(self, root_dir):
		self._generator = _dirTree(root_dir)

	def generate(self):
		tree = self._generator.build_tree()
		for entry in tree:
			print(entry)

class _dirTree(self):
	def __init__(self, root_dir):
		self._root_dir = pathlib.Path(root_dir)
		self._tree = []

	def build_tree(self):
		self._tree_head()
		self._tree_body(self._root_dir)
		return self._tree

	def _tree_head(self):
		self._tree.append(f"{self._root_dir}{os.sep}")
		self._tree.append(PIPE)
