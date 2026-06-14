############################################## RIGHT ANGLE TRIANGLE ################################

# Right Angle Trianagle - Number with Row
def rat_number_row():
    f = open ('gokulkrishnan.txt','w+')
    f.write('Right Angle Triangle Number With Row\n')
    f.write('------------------------------------\n')
    for i in range(1,9):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_number_row()


# Right Angle Trianagle - Number with Column
def rat_number_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Number With Column\n')
    f.write('---------------------------------------\n')
    for i in range(1,9):
        for j in range(1,i+1):
            f.write(str(j))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections    
    f.close()

rat_number_col()


# Right Angle Trianagle - Star
def rat_star():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Star\n')
    f.write('-------------------------\n')
    for i in range(1,9):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_star()

# Right Angle Trianagle - Lower With Row
def rat_lower_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Lower With Row\n')
    f.write('-----------------------------------\n')
    for i in range(1,9):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_lower_row()

# Right Angle Trianagle - Lower With Colum
def rat_lower_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Lower With Column\n')
    f.write('--------------------------------------\n')
    for i in range(1,9):
        for j in range(1,i+1):
            f.write(chr(j+96))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_lower_col()

# Right Angle Trianagle - Upper With Row
def rat_upper_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Upper With Row\n')
    f.write('-----------------------------------\n')
    for i in range(1,9):
        for j in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_upper_row()

# Right Angle Trianagle - Upper With Colum
def rat_upper_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Upper With Column\n')
    f.write('--------------------------------------\n')
    for i in range(1,9):
        for j in range(1,i+1):
            f.write(chr(j+64))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()  

rat_upper_col()

# Right Angle Trianagle - Name With Row
def rat_name_row():
    name='gokulkrishan'
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Name With Row\n')
    f.write('-----------------------------------\n')
    for i in range(len(name)):
        for j in range(i+1):
            f.write(name[i])
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_name_row()

# Right Angle Trianagle - Name With Column
def rat_name_col():
    name='gokulkrishan'
    f = open ('gokulkrishnan.txt','a+')
    f.write('Right Angle Triangle Name With Column\n')
    f.write('--------------------------------------\n')
    for i in range(len(name)):
        for j in range(i+1):
            f.write(name[j])
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

rat_name_col()

# Inverse Right Angle Triangle - Number With Row
def irat_number_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Number With Row\n')
    f.write('--------------------------------------------\n')
    for i in range(9,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_number_row()

# Inverse Right Angle Triangle - Number With Column
def irat_number_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Number With Column\n')
    f.write('-----------------------------------------------\n')
    for i in range(10,0,-1):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_number_col()

# Inverse Right Angle Triangle - Star
def irat_star():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Star\n')
    f.write('---------------------------------\n')
    for i in range(9,0,-1):
        for j in range(0,i):
            f.write(str('*'))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_star()

# Inverse Right Angle Trianagle - Lower With Row
def irat_lower_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Lower With Row\n')
    f.write('-------------------------------------------\n')
    for i in range(9,0,-1):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_lower_row()

# Inverse Right Angle Trianagle - Lower With Colum
def irat_lower_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Lower With Column\n')
    f.write('----------------------------------------------\n')
    for i in range(9,0,-1):
        for j in range(1,i+1):
            f.write(chr(j+96))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_lower_col()

# Inverse Right Angle Trianagle - Upper With Row
def irat_upper_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Upper With Row\n')
    f.write('-------------------------------------------\n')
    for i in range(9,0,-1):
        for j in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_upper_row()

# Inverse Right Angle Trianagle - Upper With Colum
def irat_upper_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Upper With Column\n')
    f.write('----------------------------------------------\n')
    for i in range(9,0,-1):
        for j in range(1,i+1):
            f.write(chr(j+64))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_upper_col()

# Inverse Right Angle Trianagle - Name With Row
def irat_name_row():
    name='gokulkrishan'
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Name With Row\n')
    f.write('------------------------------------------\n')
    for i in range(len(name)-1,-1,-1):
        for j in range(0,i+1):
            f.write(name[i])
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

irat_name_row()

# Inverse Right Angle Trianagle - Name With Column
def irat_name_col():
    name='gokulkrishan'
    f = open ('gokulkrishnan.txt','a+')
    f.write('Inverse Right Angle Triangle Name With Column\n')
    f.write('---------------------------------------------\n')
    for i in range(len(name)-1,-1,-1):
        for j in range(0,i+1):
            f.write(name[j])
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.write('\n')
    f.write('\n')
    f.close()

irat_name_col()

############################################## LEFT ANGLE TRIANGLE #################################

# Left Angle Trianagle - Number with Row
def lat_number_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Left Angle Triangle Number With Row\n')
    f.write('-----------------------------------\n')
    for i in range(1,9):
        for j in range(9,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

lat_number_row()


# Left Angle Trianagle - Number with Column
def lat_number_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Left Angle Triangle Number With Column\n')
    f.write('--------------------------------------\n')
    for i in range(1,9):
        for j in range(9,i,-1):
            f.write(' ')
        for k in range(1,i+1):
            f.write(str(k))
        f.write('\n')
    f.write('\n') # It adds space bewtween sections    
    f.close()

lat_number_col()


# Left Angle Trianagle - Star
def lat_star():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Left Angle Triangle Star\n')
    f.write('-------------------------\n')
    for i in range(1,9):
        for j in range(9,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

lat_star()

############################################## PYRAMID TRIANGLE #################################

# Pyramid Trianagle - Number with Row
def pat_number_row():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Pyramid Triangle Number With Row\n')
    f.write('--------------------------------\n')
    for i in range(1,9):
        for j in range(9,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

pat_number_row()


# Pyramid Trianagle - Number with Column
def pat_number_col():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Pyramid Triangle Number With Column\n')
    f.write('-----------------------------------\n')
    for i in range(1,9):
        for j in range(9,i,-1):
            f.write(' ')
        for k in range(1,i+1):
            f.write(str(k)+' ')
        f.write('\n')
    f.write('\n') # It adds space bewtween sections    
    f.close()

pat_number_col()


# Pyramid Trianagle - Star
def pat_star():
    f = open ('gokulkrishnan.txt','a+')
    f.write('Pyramid Triangle Star\n')
    f.write('---------------------\n')
    for i in range(1,9):
        for j in range(9,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('* ')
        f.write('\n')
    f.write('\n') # It adds space bewtween sections
    f.close()

pat_star()

