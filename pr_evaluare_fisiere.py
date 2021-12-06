with open('c:/Users/User/Desktop/input.txt', 'r') as f:
    copii=list(f)
m=0
print('Nr.  Numele  Prenumele  Nota1  Nota2  Nota3')
with open('c:/Users/User/Desktop/rezerva.txt', 'w') as g:
    with open('c:/Users/User/Desktop/output.txt', 'w') as d:
        for i in copii:
            campuri=i.split()
            print(i,end='')
            g.write(i+'\n')
            m=(float(campuri[3])+float(campuri[4])+float(campuri[5]))/3
            d.write(campuri[0]+'\t'+campuri[1]+'\t'+campuri[2]+'\t'+str(m)+'\n')
with open('c:/Users/User/Desktop/output.txt', 'r') as f:
    medii=list(f)
print('\n')
print('Nr.', 'Numele', 'Prenumele', 'Media', sep='\t')
for i in medii:
    medie=i.split()
    print(i)