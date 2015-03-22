import os, shutil
from sys import maxint

#change according to needs
target_directory = "portable"
delimiter = ','
new_delimiter = ','
trailing_delimiter = '' # trailing padding
new_trailing_delimiter = ''
ratio_print = 0.2
lines_max = maxint # alternatively some lower limit
attr_list = ['name','pop1996']
fileStr = 'bctop10.csv'


def file_len(file):
    return sum(1 for line in open(file))

def is_csv(file,delimiter):
    return True 

def parse_line(file,delimiter,attrs):
    with open(file) as f:
	head, tail = os.path.split(os.path.abspath(file))
        while True:
            line = f.readline()
            if not line:
                break
            s_list = string.split(line,delimiter)
            
def commasep(file):
    if not is_csv(file,delimiter):
        return
    try:
        head, tail = os.path.split(os.path.abspath(file))
        dir_name = os.path.join(head, target_directory)
        if not os.path.exists(dir_name):
            print "Creating directory " + target_directory
            os.makedirs(dir_name)
        file_name = os.path.join(dir_name, tail)
        file_length = file_len(file)
        print('File length: ' + str(file_length) + ' lines.')
        open(file_name,'a')
        with open(file,'r') as f:
            with open(file_name,'w') as o:
                head, tail = os.path.split(os.path.abspath(file))
                line = f.readline()
                if not line:
                    return
                line = line.strip();
                s_list = line.split(delimiter)
                s_to_write = '';
                i=0;
                attr_idx = [];
                for attr in attr_list:
                    print('Attribute ' + attr + ' in list.')
                for attr in s_list:
                    i+=1
                first_idx = 1;
                last_idx = i;
                i=0
                for attr in s_list:
#                   if not trailing_delimiter=='':
                    if i==first_idx:
                        attr = attr.replace(trailing_delimiter,'',1);
                    elif i==last_idx:
                        attr = attr[::-1].replace(trailing_delimiter,'',1)[::-1]
                    if attr in attr_list:
                        attr_idx.append(i);
                        print('Attribute ' + attr + ' found!')
                    else:
                        print('Attribute ' + attr + ' ignored.')
                    i+=1
                for idx in attr_idx:
                    s_to_write = s_to_write+s_list[idx] + new_delimiter;
                s_to_write = new_trailing_delimiter + s_to_write[:-len(new_delimiter)] + new_trailing_delimiter + '\n';
                o.write(s_to_write)
            with open(file_name,'a') as o:
		i=0
                next_ratio = ratio_print
                print(str(float(0)) + '% processed.')
                while i < lines_max:
                    i=i+1
                    if float(i)/file_length >= next_ratio:
                        print(str(next_ratio*100) + '% processed.')
                        next_ratio+=ratio_print
                    s_to_write = '';
                    line = f.readline()
                    if not line:
                        print('File ended.')
                        return
                    line = line.strip();
                    s_list = line.split(delimiter)
                    for idx in attr_idx:
                        s_to_write = s_to_write+s_list[idx] + new_delimiter;
                    s_to_write = new_trailing_delimiter + s_to_write[:-len(new_delimiter)] + new_trailing_delimiter + '\n';
                    o.write(s_to_write);                  
    except:
        print "Could not open " + file


commasep(fileStr)
print "Operations completed without errors."
