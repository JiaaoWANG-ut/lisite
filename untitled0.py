####分子筛三号位点探索工程

import numpy as np
from ase import Atoms, neighborlist
from ase.io import read

# 读取CIF文件
filename = "1.cif"  # 用你的CIF文件名替换
atoms = read(filename)
cell = np.array(atoms.get_cell())



# 计算邻近原子列表
custom_cutoff_radius = 3.4  # 更改为所需的截断半径值
cutoff = np.full(len(atoms), custom_cutoff_radius)
#cutoff = neighborlist.natural_cutoffs(atoms)
nl = neighborlist.NeighborList(cutoff, self_interaction=False, bothways=True)
nl.update(atoms)



###得到所有的O bond, 距离控制在3.4A经验范围
bond=[]
# 遍历所有原子，找到每个原子的近邻原子列表
for atom in atoms:
    atom_index = atom.index
    atom_symbol = atom.symbol
    atom_position = atom.position

    # 获取邻近原子索引
    neighbors_indices = nl.get_neighbors(atom_index)[0]

    #print(f"原子 {atom_index} ({atom_symbol}):")
    #print(f"  位置: {atom_position}")

    # 输出邻近原子的元素符号和位置
    #print(f"  近邻原子:")
    dist_list=[]
    for neighbor_index in neighbors_indices:
        neighbor_atom = atoms[neighbor_index]
        neighbor_symbol = neighbor_atom.symbol
        neighbor_position = neighbor_atom.position
        dist=np.linalg.norm(neighbor_position-atom_position)
        if dist < 3 and neighbor_symbol == 'O':
            #print(f"    原子 {neighbor_index} ({neighbor_symbol}):")
            #print(f"      位置: {neighbor_position}",dist)
            bond.append([atom_position,neighbor_position])

###计算bond中点位置
bond_middle_list=[]
for i in bond:
    bond_middle=(i[0]+i[1])/2
    bond_middle_list.append(bond_middle)
    
bond_middle_list=np.array(bond_middle_list)
bond_middle_list=np.unique(bond_middle_list, axis=0)





from plot_from_lattice_and_points import *

from nlist import *

def calculate_point_along_vector(p1, p2, d):

    # 计算从点 p1 指向点 p2 的单位向量 d_hat
    d = p2 - p1
    d_hat = d / np.linalg.norm(d)

    # 计算点 p3 的坐标
    p3 = p1 + d_hat * d

    return p3




lisite=[]


# for target_position in bond_middle_list:
#     neighbor=get_nlist_from_pos(atoms,1.5,target_position)
#     for i in neighbor:
#         if "Si" in i or "Al" in i:
#             p1=target_position
#             p2=i[1]
#             d=1.79
#             p3 = calculate_point_along_vector(p1, p2, d)
#             lisite.append(p3)
#             print(p3)



def get_li_site(target_position):
    atoms = read(filename)
    neighbor=get_nlist_from_pos(atoms,1.5,target_position)
    for i in neighbor:
        if "Si" in i or "Al" in i:
            p1=target_position
            p2=i[1]
            d=1.79
            p3 = calculate_point_along_vector(p1, p2, d)
            
    return p3




import multiprocessing as mul
CORES=1

pool = mul.Pool(CORES)    
arg  = bond_middle_list              ####并行输入的列表
rel  = pool.map(get_li_site,arg)     ####并行输入的函数



#plot_lattice(cell, bond_middle_list)

###可视化bond中点位置

            
            
# atoms = ase.io.read('example.cif')

# # Get the lattice vectors as a numpy array
# lattice = np.array(atoms.get_cell())
