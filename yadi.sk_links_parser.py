import os
import re

def extract_yadi(path):
#for a given directory will parse *.html files to find content links
#generates a text file with links
#also generates a launcher for the links to be opened in Chorme.

  output1=path+'links_list.txt'
  output2=path+'links_launcher.bat'
  links=[]

  filenames = os.listdir(path)
  for filename in filenames:
    print filename
    #f=path+filename
    #f.read
    f = open(path+filename, 'rU')
    for line in f:   ## iterates over the lines of the file
        #print line,    ## trailing , so print does not add an end-of-line char
        match = re.search("http://yadi.sk/[\w\.-]/[\w\.-]+", line) ##
        match = re.search("https://yadi.sk/[\w\.-]/[\w\.-]+", line) ##
                   ## since 'line' already includes the end-of line.
        # If-statement after search() tests if it succeeded
        if match:
            print 'found', 
            links.append(str(match.group()))
        #else:
            #print 'did not find'
    f.close()

#writes a regular file
  s1 = open(output1, 'w')
  for link in links:
    s1.write(link+'\n')
  s1.write('Matches found: '+ str(len(links)))
  s1.close()

#writes batch launcher
  s2 = open(output2, 'w')
  for link in links:
    s2.write("start chrome " + link+'\n')
  s2.close()
  print str(len(links)) + " links found. All done."


def main():
    #will parse files in current directory
    #test_path
    #path='c:/content/'
    path=os.getcwd()+'\\'
    print path
    extract_yadi(path)

if __name__ == '__main__':
    main()

            

