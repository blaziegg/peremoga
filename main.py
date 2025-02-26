class Blocks:
    def __init__(self):
        self.blocks = {}
        self.votes = []

    def add_block(self, block):
        self.blocks[block['id']] = block["view"]

    def add_vote(self, block_id):

        self.votes.append(block_id)

    def chain(self):
        voted_blocks = [block for block in self.blocks if block in self.votes]
        sorted_blocks = sorted(voted_blocks, key=lambda x: self.blocks[x])

        result = []
        last_view = -1

        for block_id in sorted_blocks:
            current_view = self.blocks[block_id]
            if current_view == last_view + 1:
                result.append(block_id)
            last_view = current_view

        return result
