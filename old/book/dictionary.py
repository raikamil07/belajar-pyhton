d = {'satu':'ini satu', 'dua':'ini dua', 'tiga':'ini tiga'}

print("Isi dictionary d:", d)
print( d['satu'] )
print( d['dua'] )
print( d['tiga'] )

e = {'satu':1, 'dua':2, 'tiga':3}

print( e['dua'] * e['tiga'] )

e['dua'] = 20
print( e['dua'] * e['tiga'] )

f = {'name': "raihan", 'age': 20, 'riil': 3.14, 'boolean': True}

print(len(f))
print(f)
print("namaku adalah", f['name'])
print("umurku adalah", f['age'])
print("nilai riilku adalah", f['riil'])
print("nilai booleanku adalah", f['boolean'])

f['alamat'] = "pagarsih"

print(len(f))
print(f)

del f['name']
print(len(f))
print(f)