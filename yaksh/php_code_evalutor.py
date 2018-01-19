#!/usr/bin/env python
from __future__ import unicode_literals
import traceback
import pwd
import os
from os.path import join, isfile
import subprocess
import importlib

# Local imports
from .base_evaluator import BaseEvaluator
from .file_utils import copy_files, delete_files


class PhpCodeEvaluator(BaseEvaluator):
    """Tests the Php code obtained from Code Server"""
    def __init__(self, metadata, test_case_data):
        self.files = []
        self.compiled_user_answer = None
        self.compiled_test_code = None
        self.submit_code_path = ""
        self.user_output_path = ""
        self.ref_output_path = ""

        # Set metadata values
        self.user_answer = metadata.get('user_answer')
        self.file_paths = metadata.get('file_paths')
        self.partial_grading = metadata.get('partial_grading')
        # Set test case data values
        self.test_case = test_case_data.get('test_case')
        self.weight = test_case_data.get('weight')

    def teardown(self):
        # Delete the created file.
        if os.path.exists(self.submit_code_path):
            os.remove(self.submit_code_path)
        if os.path.exists(self.user_output_path):
            os.remove(self.user_output_path)
        if os.path.exists(self.ref_output_path):
            os.remove(self.ref_output_path)
        if os.path.exists(self.test_code_path):
            os.remove(self.test_code_path)
        if self.files:
            delete_files(self.files)


    def set_file_paths(self, directory, file_name):
        output_path = "{0}{1}.class".format(directory, file_name)
        return output_path


    def compile_code(self):
            if self.file_paths:
                self.files = copy_files(self.file_paths)
            if self.exec_scope:
                return None
            else:
                submitted = compile(self.user_answer, '<string>', mode='exec')
                self.exec_scope = {}
                exec(submitted, self.exec_scope)
                return self.exec_scope

    #def check_code(self):
        """ Function validates student code using instructor code as
        reference.The first argument ref_code_path, is the path to
        instructor code, it is assumed to have executable permission.
        The second argument submit_code_path, is the path to the student
        code, it is assumed to have executable permission.

        Returns
        --------

        returns (True, "Correct answer") : If the student function returns
        expected output when called by reference code.

        returns (False, error_msg): If the student function fails to return
        expected output when called by reference code.

        Returns (False, error_msg): If mandatory arguments are not files or
        if the required permissions are not given to the file(s).

        """
    """    success = False
        mark_fraction = 0.0

        proc, stdnt_out, stdnt_stderr = self.compiled_user_answer
        stdnt_stderr = self._remove_null_substitute_char(stdnt_stderr)

        # Only if compilation is successful, the program is executed
        # And tested with testcases
        if stdnt_stderr == '':
            proc, main_out, main_err = self.compiled_test_code
            main_err = self._remove_null_substitute_char(main_err)

            if main_err == '':
                ret = self._run_command(self.run_command_args, shell=True,
                                         stdin=None,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                proc, stdout, stderr = ret
                if proc.returncode == 0:
                    success, err = True, None
                    mark_fraction = 1.0 if self.partial_grading else 0.0
                else:
                    err = stdout + "\n" + stderr
            else:
                err = "Error:"
                try:
                    error_lines = main_err.splitlines()
                    for e in error_lines:
                        if ':' in e:
                            err = err + "\n" + e.split(":", 1)[1]
                        else:
                            err = err + "\n" + e
                except:
                        err = err + "\n" + main_err
        else:
            err = "Compilation Error:"
            try:
                error_lines = stdnt_stderr.splitlines()
                for e in error_lines:
                    if ':' in e:
                        err = err + "\n" + e.split(":", 1)[1]
                    else:
                        err = err + "\n" + e
            except:
                err = err + "\n" + stdnt_stderr

        return success, err, mark_fraction"""
