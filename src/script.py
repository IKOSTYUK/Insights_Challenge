from collections import Counter, defaultdict
import csv
import sys
import os

input_file = './input/complaints.csv'
output_file = './output/results.csv'


def write_file(output_filename, complaints):
    with open(output_filename, 'w') as f:
        w = csv.DictWriter(f, ('product', 'number of complaints', 'number of companies', '% of total'))
        w.writeheader()
        w.writerows({
                'product': product,
                'number of complaints': sum(Issues.values())/2,
                'number of companies': sum(Issues.values())/len(Issues),
                '% of total' : (sum(Issues.values())/len(Issues))/(sum(Issues.values())/2),
            }
             for product, Issues in sorted(complaints.items())
        )

def read_file(input_filename):
    complaints = defaultdict(Counter)
    with open(input_filename) as f:
        for row in csv.DictReader(f):
            complaints[row['Product'], row['Date received'][:4]][row['Issue']] += 1
            complaints[row['Product'], row['Date received'][:4]][row['Company']] +=1
    return complaints

def main(input_filename, output_filename):
    write_file(output_filename, read_file(input_filename))

if __name__ == '__main__':
    main(input_file, output_file)