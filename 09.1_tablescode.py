# with open ("Tables/a", "w") as f:
#     f.write('')

for i in range(2,21):
    tables =''
    for j in range(1,21):

        tables += f'{i} X {j}= {i*j}\n'
        
    with open(f'Tables/{i} table.txt','w') as f:
        f.write(f'This Table is writen by python code\n{i} table\n')
        f.write(tables)
