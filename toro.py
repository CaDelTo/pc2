from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Root process envía a cada proceso su rank
if rank == 0:
    for i in range(size):
        comm.send(i, dest=i)
else:
    pass  # Los otros procesos no hacen nada aún

# Todos los procesos (incluyendo root) reciben su número
received_number = comm.recv(source=0)

# Elevan al cuadrado
squared = received_number ** 2

# Envían el resultado al root
if rank == 0:
    results = [squared]  # Agrega el suyo
    for i in range(1, size):
        result = comm.recv(source=i)
        results.append(result)
    print(f"root received {results}")
else:
    comm.send(squared, dest=0)
