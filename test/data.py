from pandas import DataFrame

a = [[1, 2, 3], [4, 5, 6]]
data = DataFrame(a)
data.to_json()
