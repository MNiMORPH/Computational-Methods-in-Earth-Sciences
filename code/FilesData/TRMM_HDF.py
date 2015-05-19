import h5py
f = h5py.File('2B31.20131227.91787.7.h5', 'r')
for item in f.attrs.keys():
    print item + ":", f.attrs[item]
mr = f['/entry/mr_scan/mr']
i00 = f['/entry/mr_scan/I00']
print "%s\t%s\t%s" % ("#", "mr", "I00")
for i in range(len(mr)):
    print "%d\t%g\t%d" % (i, mr[i], i00[i])
f.close()
