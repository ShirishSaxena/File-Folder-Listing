import os,datetime

Version = "v2.01b (28-Jan-18)"

now = datetime.datetime.now()
get_date = now.strftime("%d-%m-%Y")

Base_File_name = os.path.basename(__file__)

OutPut_File_Name = "Directory Listing [%s].txt" %get_date
OutPut_vFile_Name = "Video Files Listing [%s].txt" %get_date

## Changes Bytes to Human readable Format ########

def sizeof_fmt(num, suffix='B'):
    for unit in [' ',' K',' M',' G','T',' P',' E',' Z']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s %s" % (num, 'Yi', suffix)
## ------------------------------------------ #####


### Get Directory Size Inc. Subdirectories Size #####
def get_size(start_path):
    total_size = 0
    count_subd = -1
    count_files = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        count_subd += 1
        for f in filenames:
            count_files += 1
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size,count_subd,count_files

## -------------------------------------------- ######



### ############# ##################         ###########
print "\nShowY Directory Lister %s" %Version
print "Support Email : me@showy.pro"
print "Works best with ASCII Char. Names\n\n\n"
print "Please choose appropriate Options :-\n"
print "1). Listing with Sub Dir,Files,Size"
print "2). Listing with Size"
print "3). Listing only names"
print "4). Listing Video Files Only With Size"
get_ans = raw_input ("Answer [Ex. 1] : ")
what_to_do = 0

if get_ans == '1' :
    print "\nListing with Sub Dir., Files,Size\n"
    what_to_do = 1
elif get_ans == '2' :
    print "\nListing with Size\n"
    what_to_do = 2
elif get_ans == '3' :
    print "\nListing only names\n"
    what_to_do = 3
elif get_ans == '4':
    print "\nListing Video Files Only With Size\n"
    what_to_do = 4
else :
    print "\nWrong Option selected : Reverting to Option 1st"
    what_to_do = 1
    
if get_ans == '1' or get_ans == '2' or get_ans == '3':
    Total_F_D = 0
    get_file = ''
    get_dir = ''
    dir_count=1
    file_count = 1
    for x in os.listdir('.'):
        if os.path.isfile(x):
            if x != OutPut_File_Name and x != Base_File_name:
                Total_F_D += 1
                if what_to_do == 1 or what_to_do == 2:
                    get_f_size = sizeof_fmt(os.path.getsize(x))
                    get_file = "%s\n%d. %s (%s)" %(get_file,file_count,x,get_f_size)
                elif what_to_do == 3:
                    get_file = "%s\n%d. %s" %(get_file,file_count,x)
                file_count +=1
        elif os.path.isdir(x):
            Total_F_D += 1
            if what_to_do == 1:
                total_size,count_subd,count_files = get_size(x)
                total_size = sizeof_fmt(total_size)
                if count_subd == 0:
                    get_dir = "%s\n%d. %s (%s) | F[%d]" %(get_dir,dir_count,x,total_size,count_files)
                else:
                    get_dir = "%s\n%d. %s (%s) | D[%d] F[%d]" %(get_dir,dir_count,x,total_size,count_subd,count_files)
            elif what_to_do == 2:
                total_size,count_subd,count_files = get_size(x)
                total_size = sizeof_fmt(total_size)
                if count_subd == 0:
                    get_dir = "%s\n%d. %s (%s)" %(get_dir,dir_count,x,total_size)
                else:
                    get_dir = "%s\n%d. %s (%s)" %(get_dir,dir_count,x,total_size)
            elif what_to_do == 3:
                get_dir = "%s\n%d. %s" %(get_dir,dir_count,x)
            dir_count +=1
        else:
            print '\n### Unkown Error ### (', x,')\n'


    print "\nDirectories :-\n\n"
    print get_dir
    print "\n\nFiles :- \n\n"
    print get_file
    print "\n\nTotal Files and Folders : %d\n\n" %Total_F_D

    Outfile = open(OutPut_File_Name,"w")

    Outfile.write("\nDirectories :-\n\n")
    Outfile.write(get_dir)
    Outfile.write("\n\nFiles :- \n\n")
    Outfile.write(get_file)
    Outfile.write("\n\nTotal Files and Folders : %d" %Total_F_D)
    Outfile.close()
elif get_ans == '4':
    ## Program Starts Here
    List_Video = ''
    count_vfiles = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for f in filenames:
            if f.endswith(('.mkv', '.mp4','.webm','.flv','.vob','.ogg','.avi','.mov','.wmv','.rm','.mpeg','m4v','.3gp')) == True:
                count_vfiles += 1
                fp = os.path.join(dirpath, f)
                f_size = os.path.getsize(fp)
                f_size = sizeof_fmt(f_size)
                List_Video = "%s\n%d. %s (%s)" %(List_Video,count_vfiles,f,f_size)
    ## Print and Save O/p
    print "\n\nVideo Files Found :-\n\n"
    print List_Video
    print "Total Video Files : %d" %count_vfiles
    Outvfile = open(OutPut_vFile_Name,"w")
    Outvfile.write("\n\nVideo Files Found :-\n\n")
    Outvfile.write(List_Video)
    Outvfile.write("Total Video Files : %d" %count_vfiles)
    Outvfile.close()
    
raw_input("\n\n###          Press Any Key to exit           ####")

