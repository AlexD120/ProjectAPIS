
class Base():

    def __init__(self, driver):
        self.driver = driver

    """МЕТОД ПРОВЕРКИ ВЕРНОГО ЗНАЧЕНИЯ В ТЕЛЕ ОТВЕТА"""
    def check_word_in_json(self, response, word):
        assert word in response.json()

    """МЕТОД ПРОВЕРКИ НЕВЕРНОГО ЗНАЧЕНИЯ В ТЕЛЕ ОТВЕТА"""
    def check_word_not_in_json(self, response, not_word):
        assert not_word not in response.json()

    """МЕТОД ПРОВЕРКИ ВЕРНОГО ЗНАЧЕНИЯ ВО ВЛОЖЕНИИ ОТВЕТА"""
    def check_word_data_json(self, value, key, expected_value):
        assert key in value and value[key] == expected_value

    """МЕТОД ПРОВЕРКИ ВЕРНОГО ЗНАЧЕНИЯ В ТЕЛЕ ОТВЕТА"""
    def check_word_in_key_json(self, response, word):
        json_data = response.json()
        assert word in json_data.values()
