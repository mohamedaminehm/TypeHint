import os
import argparse
import shutil


ap = argparse.ArgumentParser()
ap.add_argument("-pt", "--test_path", type=str, required=True,
	help="path to test file")
ap.add_argument("-f", "--folder", type=str, required=True,
	help="file's folder to annotate")
args = vars(ap.parse_args())



def generate_trace_from_test(test_path,folder_path):
    os.system('monkeytype run "%s" test' % test_path)
    shutil.copy("monkeytype.sqlite3", folder_path) 


def generate_typehints_in_folder(folder_path):
    os.chdir(folder_path)
    for filename in os.listdir("./"):
        if filename.endswith(".py"):
            print("#############################")
            f = os.path.join(folder_path, filename).split("/")[-1].split(".")[0]
            try:
                os.system('monkeytype apply %s ' % f)
                print(f"module {f} successfully annotated !")
            except:
                print(f"Enable To annotate the file {f}")


if __name__ == "__main__":
    generate_trace_from_test(args["test_path"],args["folder"])
    generate_typehints_in_folder(args["folder"])
