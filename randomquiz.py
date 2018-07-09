import random
capital = {'kerela':'tvm','tamil nadu':'chennai','karnadaka':'banglr','maharastra':'bommay'}
for quiznum in range(4):
    quizfile = open('quiz%s.txt'%(quiznum+1),'w')
    answerkeyfile = open('quiz_answer%s.txt'%(quiznum+1),'w')
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' '*20) + 'Capitals Quiz%s'%(quiznum+1))
    states = capital.keys()
    random.shuffle(states) 
    for no in range(4):
      correctans = capital[states[no]]
      wrongans = capital.values()
      del wrongans[wrongans.index(correctans)]
      wrongans = random.sample(wrongans,3)
      option = wrongans + [correctans]
      random.shuffle(option)
      quizfile.write('%s. What is the capital of %s\n' % (no + 1,states[no]))
      for i in range(4):
         quizfile.write(('%s.%s\n' % ('ABCD'[i],option[i])))
      quizfile.write('\n')
      answerkeyfile.write('%s.%s\n'% (no + 1, 'ABCD'[option.index(correctans)]))
quizfile.close()

answerkeyfile.close()

