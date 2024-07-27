import sys
import os
arg_list = []

VIABLE_FLAGS = ["-h", "-in", "-IN", "-out", "-o", "-rows", "-cols", "-gap"]
FLAGS_ARGUMENT_NUMBER = {"-h":0, "-in":100, "-IN":1, "-out":1, "-o":1, "-rows":1, "-cols":1, "-gap":1}

current_index = 0

def tokenize_cli_arguments():
    temp_flag_arguments = []
    current_flag = ""

    for arg in sys.argv[1:]:
        if arg in VIABLE_FLAGS and arg != current_flag:
            if current_flag:
                arg_list.append({current_flag : temp_flag_arguments})
                temp_flag_arguments = []
            current_flag = arg
        elif current_flag:
            temp_flag_arguments.append(arg)
        else:
            raise Exception(f' Unknown argument was passed: "{arg}"')

    arg_list.append({current_flag : temp_flag_arguments}) # last pair


def validate_cli_arguments():
    for pair in arg_list:
        #print(f"{pair}")
        for flag, arguments in pair.items():
            #print(f"{flag} with {arguments}")
            if flag != "-in" and FLAGS_ARGUMENT_NUMBER[flag] != len(arguments):
                raise Exception(f'Unexpected arguments number of flag: "{flag}"! Use -h how to use program.')
            else:
                match flag:
                    case "-in":
                        for file in arguments:
                            if os.path.isfile(file) and os.path.splitext(file)[1] in [".png",".jpeg",".jpg"]:
                                print("File exists and it's valid")
                            else:
                                raise Exception(f'Please check if "{file}" exists and has valid extension!')
                        
                    case "-IN":
                        if  os.path.exists("./"+arguments[0]): #and os.path.isdir("./"+arguments[0]):
                            print(f"{arguments[0]} exists")
                        else:
                            raise Exception(f'Cannot find "{arguments[0]}" folder!')
                        
                    #case "-out":
                    case "-o":
                        #check if string with file extension
                        pass
                    case "-rows":
                        #check if number
                        pass
                    case "-cols":
                        #check if number
                        pass
                    case "-gap":
                        #check if number
                        pass
                    case "-h":
                        pass

