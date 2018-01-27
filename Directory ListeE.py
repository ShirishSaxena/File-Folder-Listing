import os,datetime

Version = "v4.2 (29-Jan-18)"

now = datetime.datetime.now()
get_date = now.strftime("%d-%m-%Y")

Base_File_name = os.path.basename(__file__)

Root_Dir = os.getcwd()

OutPut_iFile_Name = "Image Files Listing [%s].txt" %get_date
OutPut_File_Name = "Directory Listing [%s].txt" %get_date
OutPut_Tree_Name = "Directory Tree Listing [%s].txt" %get_date
OutPut_vFile_Name = "Video Files Listing [%s].txt" %get_date
OutPut_mFile_Name = "Music Files Listing [%s].txt" %get_date

###         Function 1 : Changes Bytes to Human readable Format             ###

def sizeof_fmt(num, suffix='B'):
    for unit in [' ',' K',' M',' G','T',' P',' E',' Z']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s %s" % (num, 'Yi', suffix)
## -----------------------      Function 1 Ends     ----------------------- ###


### Function 2 : Get Directory Including Sub Dir + Size With Subd+Files Count #####
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

###     ------------------        Function 2 Ends          ------------------    ###    


##      Function 3 : Find Images from Root Directory Show in Tree   ##

def Tree_Find_Images():
    Dir_ImageTree = ''
    Total_F_Found = 0
    Total_F_Size = 0

    for dirName, subdirList, fileList in os.walk(unicode(Root_Dir)):
        T_DirTree_FCount = 0
        Dir_ImageTree = "%s\nDirectory : %s\n" %(Dir_ImageTree,dirName)
        T_Tree_size = 0
        for fname in fileList:
            if fname.endswith(('.bmp', '.gif','.img','.jpe','.jpeg','.jpg','.pcd','.png','.psd','.tiff','.raw','.svg','.ico')) == True:
            ## Size Thingy in Tree
                Total_F_Found += 1
                fp = os.path.join(dirName, fname)
                T_Tree_size += os.path.getsize(fp)
                Total_F_Size += os.path.getsize(fp)
            ## Ends Here
                Dir_ImageTree = "%s\n\t-> %s [%s]" %(Dir_ImageTree,fname,sizeof_fmt(os.path.getsize(fp)))
                T_DirTree_FCount += 1
        if T_DirTree_FCount == 0:
            Dir_ImageTree = Dir_ImageTree.replace("\nDirectory : %s\n" %dirName,'')
        else :
            Dir_ImageTree = Dir_ImageTree.replace("\nDirectory : %s\n" %dirName,'\n\nDirectory [Files : %d] [%s] : %s\n' %(T_DirTree_FCount,sizeof_fmt(T_Tree_size),dirName))
            #Dir_ImageTree = "%s\n****\t\t\t\tFiles in Dir. : %d | %s\t\t\t\t****\n" %(Dir_ImageTree,T_DirTree_FCount,sizeof_fmt(T_Tree_size))


    print Dir_ImageTree
    print "\n\n***\t\t\tTotal Files Found : %d | %s\t\t\t***\n" %(Total_F_Found,sizeof_fmt(Total_F_Size))
    OutTreefile = open(OutPut_iFile_Name ,"w")
    OutTreefile.write(Dir_ImageTree.encode('utf-8'))
    OutTreefile.write("\n\n***\t\t\tTotal Image Files Found : %d | %s\t\t\t***\n" %(Total_F_Found,sizeof_fmt(Total_F_Size)))
    OutTreefile.close()

##    ----------------------- Fucntion 3 Ends ------------------------      ##

##      Function 4 : Print Directory Tree Inc. SubD + Files + Size Total + Files Size  ##

def Tree_Dir():
    Dir_Tree = ''
    Dir_Count = 0
    All_Dir_Count = 0
    All_Dir_Size = 0
    for dirName, subdirList, fileList in os.walk(unicode(Root_Dir)):
        Dir_Count += 1
        T_DirTree_FCount = 0
        Dir_Tree = "%s\n%d.Directory : %s\n" %(Dir_Tree,Dir_Count,dirName)
        T_Tree_size = 0
        for fname in fileList:
            ## Size Thingy in Tree
            fp = os.path.join(dirName, fname)
            T_Tree_size += os.path.getsize(fp)
            ## Ends Here
            Dir_Tree = "%s\n\t-> %s [%s]" %(Dir_Tree,fname,sizeof_fmt(os.path.getsize(fp)))
            T_DirTree_FCount += 1 #Counts Only Files inside Dir
        # Get All Directory+SubD Count & Size
        '''
       if T_DirTree_FCount == 0:
            Dir_ImageTree = Dir_ImageTree.replace("\nDirectory : %s\n" %dirName,'')
        else :
            Dir_ImageTree = Dir_ImageTree.replace("\nDirectory : %s\n" %dirName,'\n\nDirectory [Files : %d] [%s] : %s\n' %(T_DirTree_FCount,sizeof_fmt(T_Tree_size),dirName))
            #Dir_ImageTree = "%s\n****\t\t\t\tFiles in Dir. : %d | %s\t\t\t\t****\n" %(Dir_ImageTree,T_DirTree_FCount,sizeof_fmt(T_Tree_size))

        '''
        All_Dir_Count += T_DirTree_FCount
        All_Dir_Size += T_Tree_size
        # Ends Here
        Dir_Tree = Dir_Tree.replace("\n%d.Directory : %s\n" %(Dir_Count,dirName),"\n\nDirectory [Files : %d] [%s] : %s\n" %(T_DirTree_FCount,sizeof_fmt(T_Tree_size),dirName))
        #Dir_Tree = "%s\n****\t\t\t\tFiles in Dir. : %d | %s\t\t\t\t****\n" %(Dir_Tree,T_DirTree_FCount,sizeof_fmt(T_Tree_size))
    #print(soup.encode("utf-8"))
    print Dir_Tree
    print "\n\n***\t\t\tTotal Files Found : %d | %s\t\t\t***\n" %(All_Dir_Count,sizeof_fmt(All_Dir_Size))
    OutTreefile = open(OutPut_Tree_Name ,"w")
    # f.write(foo.encode('utf8'))
    OutTreefile.write(Dir_Tree.encode('utf-8'))
    OutTreefile.write("\n\n***\t\t\tTotal Files Found : %d | %s\t\t\t***\n" %(All_Dir_Count,sizeof_fmt(All_Dir_Size)))
    OutTreefile.close()
    
##    ----------------------- Fucntion 4 Ends ------------------------      ##

##      Function 5 : Print Directory + File + Size [Options 1,2,3] ##   ##

def List_Dir_w_Size(what_to_do):
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
##    ----------------------- Fucntion 5 Ends ------------------------      ##

##      Function 6 : Find Video Files inside Root Dir Shows in a Tree Format inc. Size ##   ##
def Tree_Find_Videos():
    Dir_VideoTree = ''
    Total_F_Found = 0
    Total_F_Size = 0

    for dirName, subdirList, fileList in os.walk(unicode(Root_Dir)):
        T_DirTree_FCount = 0
        Dir_VideoTree = "%s\nDirectory : %s\n" %(Dir_VideoTree,dirName)
        T_Tree_size = 0
        for fname in fileList:
            if fname.endswith(('.mkv', '.mp4','.webm','.flv','.vob','.ogg','.avi','.mov','.wmv','.rm','.mpeg','m4v','.3gp')) == True:
            ## Size Thingy in Tree
                Total_F_Found += 1
                fp = os.path.join(dirName, fname)
                T_Tree_size += os.path.getsize(fp)
                Total_F_Size += os.path.getsize(fp)
            ## Ends Here
                Dir_VideoTree = "%s\n\t-> %s [%s]" %(Dir_VideoTree,fname,sizeof_fmt(os.path.getsize(fp)))
                T_DirTree_FCount += 1
        if T_DirTree_FCount == 0:
            Dir_VideoTree = Dir_VideoTree.replace("\nDirectory : %s\n" %dirName,'')
        else :
            Dir_VideoTree = Dir_VideoTree.replace("\nDirectory : %s\n" %dirName,'\n\nDirectory [Files : %d] [%s] : %s\n' %(T_DirTree_FCount,sizeof_fmt(T_Tree_size),dirName))
            #Dir_VideoTree = "%s\n****\t\t\t\tFiles in Dir. : %d | %s\t\t\t\t****\n" %(Dir_VideoTree,T_DirTree_FCount,sizeof_fmt(T_Tree_size))


    print Dir_VideoTree
    print "\n\n***\t\t\tTotal Files Found : %d | %s\t\t\t***\n" %(Total_F_Found,sizeof_fmt(Total_F_Size))
    OutTreefile = open(OutPut_vFile_Name ,"w")
    OutTreefile.write(Dir_VideoTree.encode('utf-8'))
    OutTreefile.write("\n\n***\t\t\tTotal Video Files Found : %d | %s\t\t\t***\n" %(Total_F_Found,sizeof_fmt(Total_F_Size)))
    OutTreefile.close()

##    ----------------------- Fucntion 6 Ends ------------------------      ##

##      Function 7 : Find Music Files inside Root Dir Shows in a Tree Format inc. Size ##   ##
def Tree_Find_Music():
    Dir_MusicTree = ''
    Total_F_Found = 0
    Total_F_Size = 0

    for dirName, subdirList, fileList in os.walk(unicode(Root_Dir)):
        T_DirTree_FCount = 0
        Dir_MusicTree = "%s\nDirectory : %s\n" %(Dir_MusicTree,dirName)
        T_Tree_size = 0
        for fname in fileList:
            if fname.endswith(('.aac', '.flac', '.m4p', '.mp3', '.ogg', '.wav','.pcm','.aiff','.wma')) == True:
            ## Size Thingy in Tree
                Total_F_Found += 1
                fp = os.path.join(dirName, fname)
                T_Tree_size += os.path.getsize(fp)
                Total_F_Size += os.path.getsize(fp)
            ## Ends Here
                Dir_MusicTree = "%s\n\t-> %s [%s]" %(Dir_MusicTree,fname,sizeof_fmt(os.path.getsize(fp)))
                T_DirTree_FCount += 1
        if T_DirTree_FCount == 0:
            Dir_MusicTree = Dir_MusicTree.replace("\nDirectory : %s\n" %dirName,'')
        else :
            Dir_MusicTree = Dir_MusicTree.replace("\nDirectory : %s\n" %dirName,'\n\nDirectory [Files : %d] [%s] : %s\n' %(T_DirTree_FCount,sizeof_fmt(T_Tree_size),dirName))
            #Dir_MusicTree = "%s\n****\t\t\t\tFiles in Dir. : %d | %s\t\t\t\t****\n" %(Dir_MusicTree,T_DirTree_FCount,sizeof_fmt(T_Tree_size))


    print Dir_MusicTree
    print "\n\n***\t\t\tTotal Files Found : %d | %s\t\t\t***\n" %(Total_F_Found,sizeof_fmt(Total_F_Size))
    OutTreefile = open(OutPut_mFile_Name ,"w")
    OutTreefile.write(Dir_MusicTree.encode('utf-8'))
    OutTreefile.write("\n\n***\t\t\tTotal Music Files Found : %d | %s\t\t\t***\n" %(Total_F_Found,sizeof_fmt(Total_F_Size)))
    OutTreefile.close()

##    ----------------------- Fucntion 7 Ends ------------------------      ##


#########################################################################################
######################           Main Program Starts Here      ##########################
#########################################################################################
print "\nShowY Directory Lister %s" %Version
print "Support Email : me@showy.pro"
print "Works best with ASCII Char. Names\n\n\n"

# Menu
print "Please choose appropriate Options :-\n"
print "1). Listing with Sub Dir,Files,Size"
print "2). Listing with Size"
print "3). Listing only names"
print "4). List Video Files With Size"
print "5). List Images Files with Size"
print "6). List Music Files with Size"
print "7). List Directory Tree with Files + Size"

#Get Input
get_ans = raw_input ("Answer [Ex. 1] : ")

#Set to prevent errors
what_to_do = 1

if get_ans == '1' :
    print "\nListing with Sub Dir., Files,Size\n\n"
    List_Dir_w_Size(1)
elif get_ans == '2' :
    print "\nListing with Size\n\n"
    List_Dir_w_Size(2)
elif get_ans == '3' :
    print "\nListing only names\n\n"
    List_Dir_w_Size(3)
elif get_ans == '4':
    print "\nListing Video Files Only With Size\n\n"
    Tree_Find_Videos()
elif get_ans == '5':
    print "\nListing Image Files With Size \n"
    Tree_Find_Images()
elif get_ans == '6':
    print "\nListing Music Files With Size\n"
    Tree_Find_Music()
elif get_ans == '7':
    print "\nListing Directory Tree w/ Size\n\n"
    Tree_Dir()
else :
    print "\nWrong Option selected : Reverting to Option 1st\n\n"
    List_Dir_w_Size(1)
    
raw_input("\n\n###          Press Any Key to exit           ####")

