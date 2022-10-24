import os
import os.path
import sys

meta_file = sys.argv[1]
list_file = sys.argv[2]
id_list=[]

## remove file if it exists
if os.path.isfile('Bacteroides_metadata.rep.tsv'):
    os.remove("Bacteroides_metadata.rep.tsv")

if os.path.isfile('Bacteroides_metadata.rep.selected.csv'):
    os.remove("Bacteroides_metadata.rep.selected.csv")

## create id list
for line in open(list_file).readlines():
    genome_id = line.split()[0]
    if genome_id not in id_list:
        id_list.append(genome_id)

## select representative speices
filename = "Bacteroides_metadata.rep.tsv"
for line in open(meta_file).readlines():
    genome_id = line.split('\t')[0]
    if genome_id in id_list:
        new_line = line
        with open(filename, "a") as f:
            f.write(new_line)

## extract metedata infromation as needed
selected_file = "Bacteroides_metadata.rep.selected.csv"
for new_line in open(filename).readlines():
    genome_id = new_line.split('\t')[0]
    type=new_line.split('\t')[1]
    length=new_line.split('\t')[2]
    N50=new_line.split('\t')[4]
    completeness=new_line.split('\t')[6]
    species=new_line.split('\t')[14].split('s__')[1]
    country=new_line.split('\t')[17]
    continent=new_line.split('\t')[18]
    selected_lines = "{},{},{},{},{},{},{},{}\n".format(genome_id,species,type,length,N50,completeness,country,continent)
    with open(selected_file, "a") as f:
        f.write(selected_lines)
