from load_data import *


path = "saturn-ring-fractals/data"
print("Loaded docs")

chunks = create_chunks(path)

print(chunks)
f = open("t.txt",'w')

for i in range(10):
    f.write(str(chunks[i].page_content)+"\n\n")


f.close()