import nbformat

src_path = "3.ipynb"
dst_path = "comp0264_together.ipynb"

# 读取两个 notebook
src_nb = nbformat.read(src_path, as_version=4)
dst_nb = nbformat.read(dst_path, as_version=4)

# 把 1.ipynb 的所有 cells 追加到 comp0264_together.ipynb 最后
dst_nb.cells.extend(src_nb.cells)

# 保存回目标 notebook
nbformat.write(dst_nb, dst_path)

print(f"Done. Appended {len(src_nb.cells)} cells from '{src_path}' to '{dst_path}'.")
