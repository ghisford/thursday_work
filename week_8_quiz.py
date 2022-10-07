def store_answers(answer_list:list):
    with open('answers.txt','w') as f:
        f.write(str(answer_list)
)


answers = ['D','C','D','C','D','B','A','A','A','D','B','A','B','C','D','D','C','A','A','B','D','B','A','B','B','A','A','A','B','D','B','D','B','A','B','B','D','B','A']
store_answers(answers)

