import os
import shutil

rootPath = os.path.dirname(os.path.realpath(__file__))
directories = os.listdir(rootPath)
count = 0
totalsize = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size 

def bytesto(bytes, to, bsize=1024):

    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize

    return(r)     

print bcolors.HEADER
print '####################################################'
print '######        SYMFONY CACHE CLEARNER         #######'
print '####################################################'
print ''
for directory in directories:
	if(os.path.isdir(directory)):
		list = os.listdir(rootPath+'/'+directory)
		for dir in list:
			if(dir == 'app'):
				v = os.listdir(rootPath+'/'+directory+'/app')
				for idx, i in enumerate(v):
					if(i == 'cache'):
						print ''
						count = count+1
						print bcolors.WARNING +' - '+directory + bcolors.ENDC
						stat = getFolderSize(rootPath+'/'+directory+'/app/cache/')
						size = bytesto(stat, 'm')
						totalsize = totalsize+stat
						shutil.rmtree(rootPath+'/'+directory+'/app/cache')
						print bcolors.OKGREEN +'  * Cache supprime avec succes ('+str(round(size,0))+'Mo)' + bcolors.ENDC

print ''
print bcolors.OKBLUE +'-----------------------------------------------------------------------------------'
if(totalsize > 0):
	print '  Taille total des dossiers cache '+str(round(bytesto(totalsize, 'm')))+'Mo ('+str(count)+' projets nettoyes)'
else:
	print '  Aucun projet Symfony2 ne contient de cache !'
print '-----------------------------------------------------------------------------------'
print ''
