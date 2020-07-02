#! usr/bin/python2
import os
import hashlib
ld = os.listdir("./PDFS")
l_hash = []
for i in ld:
    fname = "./PDFS/"+i
    tmp = i.split(".")
    if tmp[-1] == 'pdf':
        fhash = hashlib.md5(open(fname).read()).hexdigest()
        if fhash in l_hash:
            os.remove(fname)
        else:
            l_hash.append(fhash) 

print '[+] DONE!'
