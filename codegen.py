blockf = open("./block.txt")
b = blockf.read()
blockf.close()

codef = open("./code.txt")
c = codef.read()
codef.close()

##############################################
b1 = b
b1 = b1.replace('#1', '1')
b1 = b1.replace('#2', '0.81,0.2')

b2 = b
b2 = b2.replace('#1', '2')
b2 = b2.replace('#2', '.2,.5')

b3 = b
b3 = b3.replace('#1', '3')
b3 = b3.replace('#2', '.2,.3')

c = c.replace('#1', b1 + "\n\n" + b2 + "\n\n" + b3)
c = c.replace('#2', "f1+f2+f3")

##############################################
outf = open("C:/Users/18858/Desktop/out.txt", 'w')
outf.write(c)
outf.close()

cc_out = ""