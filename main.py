import hashTable
import time

if __name__ == '__main__':
    ht = hashTable.HashTable(999)
    hs = hashTable.HashTable(500)
    hy = hashTable.HashTable(100)
    hq = hashTable.HashTable(79)
    with open("nazwiska.txt") as file:
        Lines = file.readlines()

    KVtable = []
    for line in Lines:
        key_value = line.split()
        KVtable.append((key_value[0], key_value[1]))

    start_time = time.time()
    for v, k in KVtable:
        hq.insert(k, int(v))
    print(f"--- %s seconds --- Hashtable {hq.size}" % (time.time() - start_time))
    print("Positions occupied ", hq.filled)
    print("Positions with DEL: ", hq.table.count("DEL"))
    print("Lastnames in table ", hq.table)
    print("Length of nazwiska.txt: ", len(Lines))
    
