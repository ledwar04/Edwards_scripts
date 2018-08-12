#Opens all .gm files and prints model details for base models contributing to fit (makes top_mod files)
import numpy as np
import os
import glob
import operator
direc = raw_input("enter folder")
direc = str("/Users/ledwar04/Desktop/Research/mod_reg/"+direc)
base_num= raw_input("enter number of bases")
base_num= int(base_num)
os.chdir(direc)
for fn in list(glob.glob('*.gm*')):
    f=open(fn)
    print fn
    lines=f.read().splitlines()
    x= len(lines)
    strong_mod=[0]*x
    important=[5,6,7,25,31,49,50,51,52,53,54,55,56,57,58,59,60] #important lines of output to keep
    model=[0]*x
    for n in important:
        model[70]=str('j || x_j(%) || Mini_j(%) || Mcor_j(%) || age_j(yr) || Z_j || (L/M)_j || YAV? || Mstars component_j || a/Fe... || SSP_chi2r || SSP_adev(%) || SSP_AV || SSP_x(%)')
        model[n]=lines[n] #to keep important lines
    model=filter(lambda a:a != 0, model) #take out empty rows
#######Change this to match your base. The 63 is always right, and the second number should be 63 plus the number of bases you are using
    for i in range (63,(63+base_num)): #just the block we need
##########
        line=lines[i]
        columns=line.split()
        c=float(columns[1])
        if c != 0: #things that contribute to the final fit
#            base_name=columns[9]
#            base_name=base_name.split('_')
#            age=base_name[0]
#            age=age.split('e')
#            age=age[1]
#            m=base_name[1]
#            file_name=str('bc2003_hr_'+m+'_chab_ssp_'+age+'.spec')
#            row=str(line+'     '+file_name)
            row=line.split()
            strong_mod[i]=row
    strong_mod=filter(lambda a:a != 0, strong_mod) #take out empty rows
    strong_mod=sorted(strong_mod, key=lambda x: float(x[1]), reverse=True)#Sort
    a=len(strong_mod)
    for i in range(0,a):
        strong_mod[i]='    '.join(strong_mod[i]) #add model base file name
    model.extend(strong_mod)
    fn=str(fn)
    n=fn.replace(".gm","")
    name=str("top_mod_"+n+".in")
    f= open(name,"w")
    for ele in model:
        f.write(ele + "\n")
#Save the bottom bit as a table for plotting
    mod_name=str(n+".plt")
    f=open(mod_name, "w")
    mod_spec=[0]*x
#######Change this to match your base. This is the start of the model spectra lines (wave, flux_norm, fmod, weight). It should be 81+(3*num_bases)
    for i in range((81+3*(base_num)),x):
############
        mod_spec[i]=lines[i]
    mod_spec=filter(lambda a:a !=0, mod_spec)
    for ele in mod_spec:
        f.write(ele + "\n")
    f.close()
