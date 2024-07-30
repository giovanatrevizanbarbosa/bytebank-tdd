import pytest
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
        expected_result = 90000
        
        employee = Employee('Elon Musk', '28/06/1971', input_salary)
        
        # When
        employee.decrease_salary()
        result = employee._salary
        
        # Then
        assert result == expected_result
        
    def test_given_salary_bonus_when_2000_then_return_200(self):
        # Given
        input_salary = 2000
        expected_result = 200
        
        employee = Employee('Ada Lovelace', '10/12/1815', input_salary)
        
        # When
        result = employee.calculate_salary_bonus()
        # Then
        assert result == expected_result
        
    def test_given_calculate_salary_bonus_when_200000_return_exception(self):
        with pytest.raises(Exception):  
        # Given
            input_salary = 200000
            
            employee = Employee('Rebecca Andrade', '08/04/1999', input_salary)
            
            # When
            result = employee.calculate_salary_bonus()
            # Then
            assert result