import numpy as np

primitive = [np.array([3, 4, 5])]
A = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
B = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
C = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])
ABC = np.array([A, B, C])
limit = 5
start = 0
end = 1
while limit > 0:
    y = []
    for i in primitive[start:end]:
        y = np.dot(ABC, i)
        for j in y:
            primitive.append(j)
    start = end
    end = len(primitive)
    limit -= 1

for i in primitive:
    print(i)
