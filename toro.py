from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    for i in range(size):
        comm.send(i, dest=i)
else:
    pass 
received_number = comm.recv(source=0)
squared = received_number ** 2
if rank == 0:
    results = [squared]
    for i in range(1, size):
        result = comm.recv(source=i)
        results.append(result)
    print(f"root received {results}")
else:
    comm.send(squared, dest=0)
