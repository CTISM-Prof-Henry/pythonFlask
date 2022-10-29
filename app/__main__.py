import os
import sys
import flask

from flask import Flask, jsonify, request, Response


def main():
    app = Flask('Plagiarism detector')  # starts a flask application

    # define os métodos de acesso ao backend. Perceba que estes métodos estão
    # definidos dentro do escopo da função main, e que o servidor é definido
    # e inicializado dentro deste escopo

    @app.route('/')
    def initial_page():
        return flask.render_template('main.html')

    @app.route('/publish')
    def publish_page():
        return flask.render_template('publish.html')

    @app.route('/compare')
    def compare_page():
        return flask.render_template('compare.html')

    @app.route('/submit_classes')
    def submit_classes_page():
        return flask.render_template('submit_classes.html')

    @app.route('/teaching_plan')
    def teaching_plan_page():
        return flask.render_template('teaching_plan.html')

    @app.route('/select_assignments_folder', methods=['POST'])
    def select_assignments_folder():
        folder = request.form['textfield_folder']
        folders = os.listdir(folder)
        response = jsonify({group_name: os.path.join(folder, group_name) for group_name in folders})
        response.headers.add('Access-Control-Allow-Origin', '*')  # must always be present
        return response

    @app.route('/select_assignment', methods=['POST'])
    def select_assignment():
        id_selector = request.form['id_selector']
        folder = request.form['folder']
        assignment = request.form['assignment']

        folders = recursive_find_scripts(os.path.join(folder, assignment))

        response = jsonify({
            file_name.split(os.sep)[-1]: file_name for file_name in folders
        })

        response.headers.add('Access-Control-Allow-Origin', '*')  # must always be present
        return response

    @app.route('/publish_to_moodle', methods=['POST'])
    def publish_to_moodle():
        from publish import main as publish_main
        moodle_user = request.form['moodle_user']
        moodle_password = request.form['moodle_password']
        assignment_link = request.form['assignment_link']
        grades = request.form['grades']

        unsuccessful = publish_main(
            csv_str=grades,
            assignment_link=assignment_link,
            moodle_user=moodle_user,
            moodle_password=moodle_password
        )

        response = jsonify({'unsuccessful': unsuccessful})

        response.headers.add('Access-Control-Allow-Origin', '*')  # must always be present
        return response

    @app.route('/submit_classes_to_portal_do_professor', methods=['POST'])
    def submit_classes_to_portal_do_professor():
        from submit_classes import main as submit_classes_main
        user = request.form['user']
        password = request.form['password']
        class_url = request.form['class_url']
        class_table_text = request.form['class_table_text']
        roll_table_text = request.form['roll_table_text']

        message = ''
        success = False
        # try:
        success = submit_classes_main(
            url=class_url,
            csv_class_description=class_table_text,
            csv_roll=roll_table_text,
            user=user,
            password=password
        )
        # except Exception as e:
        #    message = str(e)

        response = jsonify({'success': success, 'message': message})

        response.headers.add('Access-Control-Allow-Origin', '*')  # must always be present
        return response

    @app.route('/submit_teaching_plan_to_portal_do_professor', methods=['POST'])
    def submit_teaching_plan_to_portal_do_professor():
        from teaching_plan import main as teaching_plan_main
        user = request.form['user']
        password = request.form['password']
        teaching_plan_url = request.form['teaching_plan_url']
        class_table_text = request.form['class_table_text']

        message = ''
        success = False
        # try:
        success = teaching_plan_main(
            url=teaching_plan_url,
            csv_class_description=class_table_text,
            user=user,
            password=password
        )
        # except Exception as e:
        #    message = str(e)

        response = jsonify({'success': success, 'message': message})

        response.headers.add('Access-Control-Allow-Origin', '*')  # must always be present
        return response

    @app.route('/compare_assignments', methods=['POST'])
    def compare_assignments():
        folder_path = request.form['folder_path']
        assignment_left = request.form['assignment_left']
        assignment_right = request.form['assignment_right']

        left_files = recursive_find_scripts(os.path.join(folder_path, assignment_left))
        right_files = recursive_find_scripts(os.path.join(folder_path, assignment_right))

        pairs = check_plagiarism(left_files, right_files, pattern=folder_path)
        json_comparison = pairs.T.to_json()

        response = Response(json_comparison)

        response.headers.add('Access-Control-Allow-Origin', '*')  # must always be present
        return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    cur_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    cur_path = os.path.join(cur_path, 'app')
    os.chdir(cur_path)

    project_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    sys.path.append(project_path)

    main()
