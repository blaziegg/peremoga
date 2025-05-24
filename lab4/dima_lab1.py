import csv

def build_chain(blocks_file, votes_file, output_file):
    blocks = {}
    with open(blocks_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            blocks[row['id']] = {'id': row['id'], 'view': int(row['view'])}

    votes = set()
    with open(votes_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            votes.add(row['block_id'])

    chain = []
    for block_id, block in blocks.items():
        if block['view'] == 0 and block_id in votes:
            chain.append(block)
            break

    if not chain:
        return

    for block_id, block in blocks.items():
        if block['view'] == 1 and block_id in votes and block['id'] != chain[0]['id']:
            chain.append(block)
            break

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'view'])
        writer.writeheader()
        writer.writerows(chain)


blocks_file = 'blocks.csv'
votes_file = 'votes.csv'
output_file = 'chain.csv'


with open(blocks_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'view'])
    writer.writeheader()
    writer.writerow({'id': '0x123', 'view': 0})
    writer.writerow({'id': '0x456', 'view': 1})
    writer.writerow({'id': '0x789', 'view': 2})

with open(votes_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['block_id'])
    writer.writeheader()
    writer.writerow({'block_id': '0x123'})
    writer.writerow({'block_id': '0x456'})
    writer.writerow({'block_id': '0x457'})

build_chain(blocks_file, votes_file, output_file)