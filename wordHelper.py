import enchant

def rec(inpar):
  if len(inpar)==2:
    return [inpar[0]+inpar[1],inpar[1]+inpar[0]]
  else:
    res=[]
    for i in range(len(inpar)):
      ar=[c for c in inpar]
      f=ar.pop(i)
      recres=rec(ar)
      res.extend([f+c for c in recres])
    return res

print("\n\n\n\t\tMain Program Start\n\t\t^^^^ ^^^^^^ ^^^^^")
s="BRING"
d = enchant.Dict("en_US")
words=rec([c for c in s])
dwords = []
[ dwords.append(w) for w in words if d.check(w) and w not in dwords]
print("\n\n\t DICT-Checked: \n")
print("\n".join(dwords))


tgtlens=[3,4]
for tgtlen in tgtlens: 
  print("\n\n\t LENGTH: ",tgtlen,"\n")
  idx=len(s)-tgtlen
  lwords = []
  [lwords.append(w[idx:]) for w in words if d.check(w[idx:])]
  print("\n".join(lwords))

spl = [w for w in words if w[3]=="S" and d.check(w) ]
print("\n\n\t SPL: \n")
print("\n".join(spl))
