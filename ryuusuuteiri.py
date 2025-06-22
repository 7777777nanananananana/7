import sympy as sp

# 複素変数と変数の定義
z = sp.symbols('z')

# 例: f(z) = 1/(z**2 + 1)
f = 1 / (z**2 + 1)

# 留数を計算したい点（例: z = sp.I）
point = sp.I

# 留数の計算
residue = sp.residue(f, z, point)

print(f"f(z) = {f}")
print(f"z = {point} における留数: {residue}")