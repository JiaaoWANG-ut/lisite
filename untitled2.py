from ase.io import read
from ase.neighborlist import NeighborList
import numpy as np

# 从cif文件中读取晶体结构
structure = read('.cif')

# 定义原子间距的半径为2埃
cutoff_radius = 3
nl = NeighborList([cutoff_radius/2]*len(structure), self_interaction=False, bothways=True)

# 计算邻居列表
nl.update(structure)

# 遍历所有原子
for i in range(len(structure)):
    # 获取原子i的近邻原子列表和距离
    neighbor_indices, neighbor_distances = nl.get_neighbors(i)

    # 输出每个近邻原子的元素、位置和距离中心原子距离
    print(f"Atom {i} neighbors:")
    for j, dist in zip(neighbor_indices, neighbor_distances):
        print(f"\tElement: {structure[j].symbol}, Position: {structure[j].position}, Distance: {dist:.3f} Å")
