import unittest
import requests

class TestFlightAPI(unittest.TestCase):
    #HTTP status code’larını kontrol et
    def test_status_code(self):
        response = requests.get('https://flights-api.buraky.workers.dev/')
        self.assertEqual(response.status_code, 200, "HTTP status kodu beklenen değerde değil.")

        #Response içeriği yazdırma
        print(response.text)

    #Response içeriğini kontrol et
    def test_response_structure(self):
        response = requests.get('https://flights-api.buraky.workers.dev/')
        json_data = response.json()

        self.assertIsInstance(json_data, dict, "Response JSON verisi bir sözlük değil.")
        self.assertIn('data', json_data, "Response JSON verisi 'data' anahtarını içermiyor.")
        self.assertIsInstance(json_data['data'], list, "Response JSON verisi 'data' liste değil.")
        for flight in json_data['data']:
            self.assertIsInstance(flight['id'], int, "Flight 'id' alanı bir tamsayı değil.")
            self.assertIsInstance(flight['from'], str, "Flight 'from' alanı bir metin değil.")
            self.assertIsInstance(flight['to'], str, "Flight 'to' alanı bir metin değil.")
            self.assertIsInstance(flight['date'], str, "Flight 'date' alanı bir metin değil.")

    #Header kontrolü
    def test_content_type_header(self):
        response = requests.get('https://flights-api.buraky.workers.dev/')
        self.assertEqual(response.headers['Content-Type'], 'application/json', "Content-Type başlığı beklenen değerde değil.")

if __name__ == '__main__':
    unittest.main()
