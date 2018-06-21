import os
import argparse
from datetime import datetime

#--------------------------------------------------------------------------------------------------
#Command line input parameters
parser = argparse.ArgumentParser(description='Definition Curator')

parser.add_argument('--i',
                    metavar='-input',
                    required=True,
                    help='input python script')
#--------------------------------------------------------------------------------------------------

def main():
    start_time = datetime.now()
    options = parser.parse_args()

    import_out = "import os\n"
    import_out += "from " + str(options.i.split("/")[-1].split(".")[0]) + " import "
    print_out = "#--------------------------------------------------------------------------------------------------\n"
    print_out += "# def curator; written by dylan fox 20180621; version 1.0.0.0\n"
    print_out += "#--------------------------------------------------------------------------------------------------\n\n"
    print_out += "#ex:\n"
    print_out += "#\tdefName(input1,input2,...,inputN)\n"
    print_out += "#\t\t#return output\n\n"
    print_out += "#--------------------------------------------------------------------------------------------------\n\n"   
    print_out += "def main():\n"

    def_found = False
    class_found = False
    class_def_found = False
    with open(options.i) as f:
        content = f.readlines()
        for c in content:
            if def_found:
                if c[0:10] == "    return":
                    print_out += "\t\t#" + str(c[4:]) + "\n"
                    def_found = False
                
                if c[0:3] == "def":

                    print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                    print_out += "\ttitle: " + str(c[4:].split("(")[0]) + "\n"
                    print_out += "\tfunction:\n"
                    print_out += "\tinput:\n"
                    print_out += "\toutput:\n"
                    print_out += "\t\'\'\'\n"
                    print_out += "\t" + str(c[4:].split(":")[0]) + "\n"
                    import_out += str(c[4:].split("(")[0]) + ", "
                elif c[0:5] == "class":
                    class_found = True
                    def_found = False
                    class_def_found = False
                    print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                    print_out += "\ttitle: " + str(c[6:].split(":")[0].split("(")[0]) + "\n"
                    print_out += "\tfunction:\n"
                    print_out += "\tinput:\n"
                    print_out += "\toutput:\n"
                    print_out += "\t\'\'\'\n"
                    print_out += "\t" + str(c[6:].split(":")[0]) + " #class\n"
                    import_out += str(c[6:].split(":")[0].split("(")[0]) + ", "

            elif class_found:
                if class_def_found:
                    if c[0:14] == "        return":
                        print_out += "\t\t\t#" + str(c[8:]) + "\n"
                        class_def_found = False
                    if c[0:7] == "    def":
                        print_out += "\n\n\t\t\'\'\'--------------------------------------------------------------------------------------------\n"
                        print_out += "\t\ttitle: " + str(c[8:].split("(")[0]) + "\n"
                        print_out += "\t\tfunction:\n"
                        print_out += "\t\tinput:\n"
                        print_out += "\t\toutput:\n"
                        print_out += "\t\t\'\'\'\n"
                        print_out += "\t\t#" + str(c[8:].split(":")[0]) + "\n"
                    if c[0:3] == "def":

                        print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                        print_out += "\ttitle: " + str(c[4:].split("(")[0]) + "\n"
                        print_out += "\tfunction:\n"
                        print_out += "\tinput:\n"
                        print_out += "\toutput:\n"
                        print_out += "\t\'\'\'\n"
                        print_out += "\t" + str(c[4:].split(":")[0]) + "\n"
                        import_out += str(c[4:].split("(")[0]) + ", "
                        class_def_found = False
                        def_found = True
                        class_found = False
                    elif c[0:5] == "class":
                        class_found = True
                        def_found = False
                        class_def_found = False
                        print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                        print_out += "\ttitle: " + str(c[6:].split(":")[0].split("(")[0]) + "\n"
                        print_out += "\tfunction:\n"
                        print_out += "\tinput:\n"
                        print_out += "\toutput:\n"
                        print_out += "\t\'\'\'\n"
                        print_out += "\t" + str(c[6:].split(":")[0]) + " #class\n"
                        import_out += str(c[6:].split(":")[0].split("(")[0]) + ", "
                else:
                    if c[0:7] == "    def":
                        class_def_found = True
                        print_out += "\n\n\t\t\'\'\'--------------------------------------------------------------------------------------------\n"
                        print_out += "\t\ttitle: " + str(c[8:].split("(")[0]) + "\n"
                        print_out += "\t\tfunction:\n"
                        print_out += "\t\tinput:\n"
                        print_out += "\t\toutput:\n"
                        print_out += "\t\t\'\'\'\n"
                        print_out += "\t\t#" + str(c[8:].split(":")[0]) + "\n"
                    if c[0:3] == "def":
                        print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                        print_out += "\ttitle: " + str(c[4:].split("(")[0]) + "\n"
                        print_out += "\tfunction:\n"
                        print_out += "\tinput:\n"
                        print_out += "\toutput:\n"
                        print_out += "\t\'\'\'\n"
                        print_out += "\t" + str(c[4:].split(":")[0]) + "\n"
                        import_out += str(c[4:].split("(")[0]) + ", "
                        class_def_found = False
                        def_found = True
                        class_found = False
                    elif c[0:5] == "class":
                        class_found = True
                        def_found = False
                        class_def_found = False
                        print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                        print_out += "\ttitle: " + str(c[6:].split(":")[0].split("(")[0]) + "\n"
                        print_out += "\tfunction:\n"
                        print_out += "\tinput:\n"
                        print_out += "\toutput:\n"
                        print_out += "\t\'\'\'\n"
                        print_out += "\t" + str(c[6:].split(":")[0]) + " #class\n"
                        import_out += str(c[6:].split(":")[0].split("(")[0]) + ", "
            else:
                if c[0:3] == "def":
                    def_found = True
                    class_found = False
                    print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                    print_out += "\ttitle: " + str(c[4:].split("(")[0]) + "\n"
                    print_out += "\tfunction:\n"
                    print_out += "\tinput:\n"
                    print_out += "\toutput:\n"
                    print_out += "\t\'\'\'\n"
                    print_out += "\t" + str(c[4:].split(":")[0]) + "\n"
                    import_out += str(c[4:].split("(")[0]) + ", "
                elif c[0:5] == "class":
                    class_found = True
                    def_found = False
                    print_out += "\n\n\t\'\'\'--------------------------------------------------------------------------------------------\n"
                    print_out += "\ttitle: " + str(c[6:].split(":")[0].split("(")[0]) + "\n"
                    print_out += "\tfunction:\n"
                    print_out += "\tinput:\n"
                    print_out += "\toutput:\n"
                    print_out += "\t\'\'\'\n"
                    print_out += "\t" + str(c[6:].split(":")[0]) + " #class\n"
                    import_out += str(c[6:].split(":")[0].split("(")[0]) + ", "
    print_out += "#--------------------------------------------------------------------------------------------------\n"
    print_out += "if __name__ == \"__main__\":\n"
    print_out += "\tmain()\n"

    print_out = str(import_out) + "\n\n" + str(print_out) 
    
    out_file = str(options.i.split(".")[0]) + "_defs.py"

    with open(out_file, 'w') as f:
        f.write(print_out)



#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()