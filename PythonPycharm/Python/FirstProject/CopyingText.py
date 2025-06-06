#Copying text from one file to another
with open('C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\read.txt', 'r') as rf:
    with open('C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\write.txt', 'a') as wf:
        for line in rf:
            wf.write(line)

#Read and print data
f=open('C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\read.txt', 'r')
file_content=f.read()
print(file_content)


# readfile = open('C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\read.txt','r')
# writefile = open('C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\write.txt', 'w')
#
# for x in readfile.readlines():
#     writefile.write(x)
#
# readfile.close()
# writefile.close()
