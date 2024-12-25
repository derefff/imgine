import sys
import os

VIABLE_FLAGS = ["-h", "-in", "-IN", "-out", "-o", "-rows", "-cols", "-gap", "-on", "-oa", "-fs", "-fontsize", "-ifc", "-inversefontcolor"]
FLAGS_ARGUMENT_NUMBER = {"-h":0, "-in":100, "-IN":1, "-out":1, "-o":1, "-rows":1, "-cols":1, "-gap":1, "-fs":1, "-fontsize":1, "-on":0, "-oa":0, "-ifc": 0, "-inversefontcolor":0}

current_index = 0

def tokenize_cli_arguments():
    temp_flag_arguments = []
    current_flag = ""
    arg_list = []

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
    return arg_list


def validate_cli_arguments(arg_list):
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
                            if not os.path.isfile(file) and not os.path.splitext(file)[-1] in [".png",".jpeg",".jpg"]:
                                raise Exception(f'Please check if "{file}" exists and has valid extension!')

                    case "-IN":
                        if not os.path.exists("./"+arguments[0]) and not os.path.isdir("./"+arguments[0]):
                            raise Exception(f'Cannot find "{arguments[0]}" folder!')

                    case "-o" | "-out":
                        if not os.path.splitext(arguments[0])[-1] in [".png",".jpeg",".jpg"]:
                            raise Exception(f'Please check if -o [filename] has valid file extension!')
                    case "-rows":
                        if not arguments[0].isnumeric():
                            raise Exception(f'Use numeric value to specify -rows!')
                    case "-cols":
                        if not arguments[0].isnumeric():
                            raise Exception(f'Use numeric value to specify -cols!')
                    case "-gap":
                        if not arguments[0].isnumeric():
                            raise Exception(f'Use numeric value to specify -gap!')
                    case "-fs" | "-fontsize":
                        if not arguments[0].isnumeric():
                            raise Exception(f'Use numeric value to specify font size!')
                    case "-on":
                      if len(arguments) > 0:
                          raise Exception(f'The flag "-on" does not accept arguments!')
                    case "-oa":
                        if len(arguments) > 0:
                            raise Exception(f'The flag "-an" does not accept arguments!')
                    case "-ifc" | "-inversefontcolor":
                        if len(arguments) > 0:
                            raise Exception(f'The flag "-ifc"/ "-inversefontcolor" does not accept arguments!')
