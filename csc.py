import os, shutil

#change according to needs
target_directory = "portable"
delimiter = ','
attr_list = ['name','pop1996']
fileStr = 'bctop10.csv'

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
                for attr in s_list:
                    if attr in attr_list:
                        attr_idx.append(i);
                    i=i+1;
                for idx in attr_idx:
                    s_to_write = s_to_write+s_list[idx] + delimiter;
                s_to_write = s_to_write[:-1] + '\n';
                o.write(s_to_write)
            with open(file_name,'a') as o:
                while True:
                    s_to_write = '';
                    line = f.readline()
                    if not line:
                        return
                    line = line.strip();
                    s_list = line.split(delimiter)
                    for idx in attr_idx:
                        s_to_write = s_to_write+s_list[idx] + delimiter;
                    s_to_write = s_to_write[:-1] + '\n';
                    o.write(s_to_write);                  
    except:
        print "Could not open " + file


commasep(fileStr)
print "Operations completed without errors."
