import os, shutil

def deploy_static_to_public():
    static_path = '../porter/static/'
    destination_path = '../porter/docs/'
    #public_path = '../porter/public/'

    #if os.path.exists(static_path):
    #    print("STATIC CONTENTS: ", os.listdir(static_path))
    #else:
    #    raise ValueError("../porter/static directory does not exist!!!")
    #if os.path.exists(public_path):
    #    print("PUBLIC CONTENTS: ", os.listdir(public_path))
    #else:
    #    raise ValueError("../porter/public directory does not exist!!!")
    
    delete_public_directory(destination_path)
    create_public_directory(destination_path)
    copy_static_directory(static_path, destination_path)

def delete_public_directory(destination_path):
    try:
        #print("Deleting Public Directory!")
        shutil.rmtree(destination_path)
    except Exception as error:
        print(error)

def create_public_directory(destination_path):
    try:
        #print("Creating Public Directory!")
        os.mkdir(destination_path)
    except Exception as error:
        print(error)

def copy_static_directory(static_path, destination_path):
    file_list = os.listdir(static_path)
    for file in file_list:
        #print(file)
        static_copy = os.path.join(static_path, file)
        public_copy = os.path.join(destination_path, file)
        #print(static_copy)
        #print(public_copy)
        if os.path.isfile(static_copy):
            #print("enter file copy logic")
            shutil.copy(static_copy, public_copy)
        elif os.path.isdir(static_copy):
            #print("enter directory copy logic")
            os.mkdir(public_copy)
            copy_static_directory(static_copy, public_copy)
