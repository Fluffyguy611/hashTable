import hashTable
import time

if __name__ == '__main__':
    ht = hashTable.HashTable(27)
    hs = hashTable.HashTable(500)
    hy = hashTable.HashTable(100)
    hq = hashTable.HashTable(80)
    with open("nazwiska.txt") as file:
        Lines = file.readlines()

    KVtable = []
    for line in Lines:
        key_value = line.split()
        KVtable.append((key_value[0], key_value[1]))

    start_time = time.time()
    for v, k in KVtable:
        ht.insert(k, int(v))
    print("--- %s seconds --- Hashtable 1000" % (time.time() - start_time))
    print("Pozycji usunietych: ", ht.DEL)
    print("Pozycje zapełnione ", ht.filled)
    print("Dlugosc nazwisk.txt: ", len(Lines))

    start_time = time.time()
    for v, k in KVtable:
        hs.insert(k, int(v))
    print("--- %s seconds --- Hashtable 500" % (time.time() - start_time))

    start_time = time.time()
    for v, k in KVtable:
        hy.insert(k, int(v))
    print("--- %s seconds --- Hashtable 100" % (time.time() - start_time))

    start_time = time.time()
    for v, k in KVtable:
        hq.insert(k, int(v))
    print("--- %s seconds --- Hashtable 50" % (time.time() - start_time))


