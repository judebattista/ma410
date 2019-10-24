base = int(input('Base:'))
modulus = int(input('Modulus:'))

vals = []
labels = []
indices = range(1, 11);
for ndx in indices:
    val = base**ndx % modulus
    vals.append(val)
    label = '{0}^{1} % {2} = {3}'.format(base, ndx, modulus, val)
    labels.append(label)
    print(label)
