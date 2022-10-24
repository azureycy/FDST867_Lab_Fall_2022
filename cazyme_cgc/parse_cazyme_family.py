# families annotated for each CAZyme protein
import os
import sys


def update_cgcout(input_dir, output_file):
    with open(output_file, 'a') as out_file:
        out_file.write('genome_id,gene_id,CAZyme_family,CAZyme_class' + '\n')
        for dirpath, dirnames, filenames in os.walk(input_dir):
            for genome_id in dirnames:
                for line in open(input_dir + '/' + genome_id + '/overview.txt').readlines()[1:]:
                    line = line.strip().split('\t')
                    gene_id = line[0]
                    hmmer = line[2]
                    ecami = line[3]
                    num_tools = int(line[5])
                    if num_tools >= 2:
                        if hmmer != '-':
                            if '+' in hmmer:
                                hmmer_list = hmmer.split('+')
                                for j in range(len(hmmer_list)):
                                    hmmer_list[j] = hmmer_list[j].split('(')[0]
                                    if 'GT2_' in hmmer_list[j]:
                                        hmmer_list[j] = 'GT2'
                                    if 'CBM35inCE17' in hmmer_list[j]:
                                        hmmer_list[j] = 'CBM35'
                                    cazy_class = hmmer_list[j].rstrip('0123456789_')
                                    out_file.write(genome_id + ',' + gene_id + ',' + hmmer_list[j] + ',' + cazy_class + '\n')
                            else:
                                hmmer = hmmer.split('(')[0]
                                if 'GT2_' in hmmer:
                                    hmmer = 'GT2'
                                if 'CBM35inCE17' in hmmer:
                                    hmmer = 'CBM35'
                                cazy_class = hmmer.rstrip('0123456789_')
                                out_file.write(genome_id + ',' + gene_id + ',' + hmmer + ',' + cazy_class + '\n')
                        elif ecami != '-':
                            if '+' in ecami:
                                ecami_list = ecami.split('+')
                                for j in range(len(ecami_list)):
                                    if 'GT2_' in ecami_list[j]:
                                        ecami_list[j] = 'GT2'
                                    if 'CBM35inCE17' in ecami_list[j]:
                                        ecami_list[j] = 'CBM35'
                                    cazy_class = ecami_list[j].rstrip('0123456789_')
                                    out_file.write(genome_id + ',' + gene_id + ',' + ecami_list[j] + ',' + cazy_class + '\n')
                            else:
                                if 'GT2_' in ecami:
                                    ecami = 'GT2'
                                if 'CBM35inCE17' in ecami:
                                    ecami = 'CBM35'
                                cazy_class = ecami.rstrip('0123456789_')
                                out_file.write(genome_id + ',' + gene_id + ',' + ecami + ',' + cazy_class + '\n')
                        else:
                            print(genome_id, gene_id, ' error!!!')
        out_file.close()


if __name__ == "__main__":
    input_dir = sys.argv[1]   # dbcan output directory
    output_file = sys.argv[2] + '/cazyme_family.csv'

    if os.path.exists(output_file):
        os.remove(output_file)

    update_cgcout(input_dir, output_file)

# python3 parse_cazyme_family.py dbcan_out .
