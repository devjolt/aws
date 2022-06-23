for i in range(1, 11):
    with open(f'cp{i}.py', 'w+') as f:
        f.writelines(
            [
                '"""',
                'multi_option_from_correct_incorrect\n',
                'make_items_question_from_correct_incorrect\n',
                'make_items_question_from_pairs\n',
                'posneg_pairs\n',
                'new_pairs\n',
                'multi_option_pairs\n',
                'order_from_pairs\n',
                'code_block_question\n',
                '"""\n\n',
                'questions = {\n',
                '}'
            ]
        )
