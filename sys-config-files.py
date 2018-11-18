#!/usr/bin/python3

import shutil
import apt_pkg
import apt_inst
import apt
import apt.debfile
import apt.progress
import aptsources.distinfo
import os.path
from pathlib import Path

cache = apt.Cache()
for pkg in cache:
    if not pkg.installed:
        continue

    ver = pkg.installed
    try:
        x = ver.fetch_binary("pkg")
    except:
        continue
    
    package = apt.debfile.DebPackage(x)
    ar = apt_inst.DebFile(x)
    tarfile = ar.data
    
    for file in pkg.installed_files:
        if not os.path.isdir(file):
            if file.startswith('/etc'):
                p = Path("." + file)
                p2 = Path("./temp").joinpath(pkg.name)
                p3 = p2.joinpath(p)
                if not p3.parent.exists():
                    p3.parent.mkdir(parents=True)
                try:
                    data = tarfile.extractdata(file[1:])
                    with p3.open('wb') as f:
                        f.write(data)
                except Exception as ex:
                    print(ex)

                    
#                shutil.copyfile(file, p3)
        
exit

apt_pkg.init()
cache = apt_pkg.Cache(None)
for k in cache.packages:
    if k.current_ver:
        print(k.name)
        ver = k.current_ver
        for (file, i) in ver.file_list:
            print(i, "\t", file.filename)

if False:
    cache = apt.Cache()
    cache.update()
    cache.open(None)
    cache.upgrade(True)
    cache.commit()



