from multiprocessing import Process, Value
from time import sleep

n = 10
clock = [Value('i', 0) for i in range(n)]  # logical clocks for each process
request = [Value('i', 0) for i in range(n)]  # request flags for each process


def request_cs(pid):
    request[pid].value = 1
    clock[pid].value += 1
    for j in range(n):
        if j != pid:
            while request[j].value == 1:
                if clock[j].value < clock[pid].value:
                    clock[pid].value += 1
                elif (clock[j].value == clock[pid].value) and (j < pid):
                    clock[pid].value += 1
        else:
            break
    print(f"Process {pid} enters critical section at {clock[pid].value}")
    sleep(1)  # simulate critical section
    print(f"Process {pid} exits critical section")
    request[pid].value = 0


if __name__ == '__main__':
    processes = [Process(target=request_cs, args=(i,)) for i in range(n)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()