#6 task
non_unique_names = ['Juli Roberts', 'Michael Mitchell', 'Max Peterson',  'Max Mitchell', 'John Mitchell', 'Juli Roberts','Maria Mitchell', 'Max Peterson', 'Juli Roberts']
non_duplicate_names = list(dict.fromkeys(non_unique_names))
print(non_duplicate_names)
