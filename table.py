import os
import glob
import operator

BCG= raw_input("Enter BCG name")
RUN= raw_input("Enter run #")

os.chdir(str('/Users/ledwar04/Desktop/Research/mod_reg/'+BCG+'/run'+RUN))
for point in ['core','cent','out','outsk','icl']:
        fn= str('4top_'+BCG+point+'.in')
        filen= fn.split('_')
        filen= filen[1]
        filen= filen.split('.')

        try:
            f=open(fn)
            lines=f.read().splitlines()
            x=len(lines)
            age=[0]*x
            metal=[0]*x
            alpha=[0]*x
            for l in range(0,x):
                line=lines[l]
                col=line.split()
                percent= float(col[0])/100.0
                age[l]= float(col[1])*percent
                metal[l]= float(col[2])*percent
                alpha[l]= float(col[3])*percent
                age_x= sum(age)
                metal_x= sum(metal)
                alpha_x= sum(alpha)

            filename= str('age_avg.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= str(age_x)
            f.write(ele + '\n')
            f.close

            filename= str('metal_avg.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= str(metal_x)
            f.write(ele + '\n')
            f.close
               
            filename= str('alpha_avg.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= str(alpha_x)
            f.write(ele + '\n')
            f.close

        except IOError as e:
            filename= str('age_avg.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close

            filename= str('metal_avg.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close

            filename= str('alpha_avg.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close

            filename= str('error.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close

            filename= str('sn.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close
  
            filename= str('vd.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close

            filename= str('vo.'+filen[0]+'.'+filen[1])
            f=open(filename, 'w')
            ele= '-99'
            f.write(ele + '\n')
            f.close
