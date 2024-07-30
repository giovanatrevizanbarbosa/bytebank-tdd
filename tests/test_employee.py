from model.employee import Employee

class TestEmployee:
    def test_given_birth_date_when_18_04_2005_then_return_19(self):
        # Given
        input = '18/04/2005'
        expected_result = 19
        
        employee = Employee('Someone', input, 1000)
        
        # When
        result = employee.age()
        
        # Then
        assert result == expected_result
        
    def test_given_fullname_when_Giovana_Trevizan_then_return_Trevizan(self):
        # Given
        input = 'Giovana Trevizan'
        expected_result = 'Trevizan'
        
        employee = Employee(input, '18/04/2005', 1000)
        
        # When
        result = employee.surname()
        
        # Then
        assert result == expected_result
        
    def test_given_salary_decrease_when_100000_then_return_90000(self):
        # Given
        input_salary = 100000
        input_fullname = 'Elon Musk'
        expected_result = 90000
        
        employee = Employee(input_fullname, '28/06/1971', input_salary)
        
        # When
        employee.decrease_salary()
        result = employee._salary
        
        # Then
        assert result == expected_result