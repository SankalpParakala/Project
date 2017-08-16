import json
import pip
import sys

def read_json_dependencies():
        with open(sys.argv[1]) as data_file:
                data = json.load(data_file)

        return data.get('Dependencies')

def install_dependencies(dependencies):
        unsuccessful_installations = 0
        for dependency in dependencies:
                failed_download = pip.main(['-q', 'download', dependency])
                failed_install = pip.main(['-q', 'install', dependency])
                if failed_download or failed_install:
                        print "Failed to install package: %s" % dependency
                        unsuccessful_installations += 1
        if unsuccessful_installations == 0:
            print "Success!!!"

if __name__=="__main__":
        dependencies = read_json_dependencies()
        install_dependencies(dependencies)
