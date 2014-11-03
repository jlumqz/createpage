
import os
filenames=os.listdir('/var/www/html/')

basedir='/var/www/html/'

findex=open(basedir+'index.html','w')

for filename in filenames:
    if filename.endswith('.json') == False:
        continue
    print >>findex,'<a target="_blank" href="'+filename+'.html">'+filename+'.html</a><br/>'
    
    fout=open(basedir+filename+'.html','w')
    print >>fout,open('/home/meng/papershow/html.template.1').read(),
    print >>fout,filename,
    print >>fout,open('/home/meng/papershow/html.template.2').read()
    fout.close()
    
findex.close()

print 'OVER'






