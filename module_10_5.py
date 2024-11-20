import multiprocessing
import time


def read_info(name):
    with open(name, 'r') as file:
        all_data = [line for line in file]


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = time.time()
for i in filenames:
    read_info(i)
print(str(time.time()-start) + '(линейный)')

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        start = time.time()
        x = pool.map(read_info, filenames)
        print(format(time.time() - start))
