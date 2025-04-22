from main import Blocks

class BlockInput:
    def __init__(self):
        self.blocks = Blocks()

    def info_input(self):

        while True:
            block_id_input = input("Введіть ID блоку (або 'next', щоб почати вводити голоси): ")

            if block_id_input.lower() == 'next':
                break

            try:
                block_id = int(block_id_input)
                view = int(input("Введіть view для блоку: "))

                new_block = {
                    'id': block_id,
                    'view': view
                }

                self.blocks.add_block(new_block)
            except ValueError:
                print("Некоректне значення, спробуйте ще раз.")

        while True:
            vote_input = input("Введіть голос або 'exit' для завершення голосування: ")

            if vote_input == "exit":
                break

            vote_id = int(vote_input)
            self.blocks.add_vote(vote_id)

        sorted_blocks = self.blocks.chain()
        print("Ланцюг блоків:")
        for block_id in sorted_blocks:
            print(f"id {block_id}, view: {self.blocks.blocks[block_id]}")
if __name__ == "__main__":
    block_input = BlockInput()
    block_input.info_input()