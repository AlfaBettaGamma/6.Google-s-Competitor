def WordSearch(len, s, subs):
  stNew = []
  count = 0
  p = 0
  lfp = - 1
  fp = 0
  rf = 0
  for char in s:
    count += 1

  while p < count:
    if s[p] == ' ':
      lfp = p

    if p - fp == len + 1:
      if lfp == -1:
        stNew.append(s[fp:p - 1])
        rf += 1
        fp = p - 1
        p -= 1
      else:
        stNew.append(s[fp:lfp])
        rf += 1
        fp = lfp + 1
        p = lfp + 1
        lfp -= 1
    p += 1

  if p > fp:
    stNew.append(s[fp:p])
    rf += 1
    
  fin = []
    
  for i in range(rf):  
    if subs in stNew[i].split():       
        fin.append(1)        
    else:        
        fin.append(0)       

  return fin

WordSearch(12,' строка разбивается на набор строк через выравнивание по заданной ширине.','строк')
