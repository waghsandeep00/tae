
class UtilFunctions(object):

    @staticmethod
    def compare_list(actual_list,expected_list):
        actual_list.sort()
        expected_list.sort()
        if actual_list == expected_list:
            return True
        else:
            return False
