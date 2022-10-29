import os
import sys


if __name__ == '__main__':
    cur_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    cur_path = os.path.join(cur_path, 'app')
    os.chdir(cur_path)

    project_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    sys.path.append(project_path)

    main()
