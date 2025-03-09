import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import time

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# No modificar
def retrieve_phone_code(driver) -> str:
    import json
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                logging.info(f"Código de confirmación obtenido: {code}")
        except WebDriverException as e:
            logging.warning(f"Error al obtener el código: {e}")
            time.sleep(1)
            continue
        if code:
            return code

    raise Exception("No se encontró el código de confirmación del teléfono.")

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        logging.info(f"Estableciendo la dirección de origen: {from_address}")
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)
        time.sleep(9)

    def set_to(self, to_address):
        logging.info(f"Estableciendo la dirección de destino: {to_address}")
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)
        time.sleep(9)

    def get_from(self):
        logging.info("Obteniendo la dirección de origen.")
        value = WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.from_field)
        ).get_property('value')
        time.sleep(9)
        return value

    def get_to(self):
        logging.info("Obteniendo la dirección de destino.")
        value = WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.to_field)
        ).get_property('value')
        time.sleep(9)
        return value

    def set_route(self, address_from, address_to):
        logging.info("Estableciendo la ruta.")
        self.set_from(address_from)
        self.set_to(address_to)
        time.sleep(9)

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        logging.info("Iniciando prueba: establecer ruta.")
        self.driver.get(data.urban_routes_url)
        time.sleep(9)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(9)

    def test_select_comfort_tariff(self):
        logging.info("Iniciando prueba: seleccionar tarifa Comfort.")
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 9).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'comfort-tariff'))
        ).click()
        time.sleep(9)

    def test_fill_phone_number(self):
        logging.info("Iniciando prueba: rellenar número de teléfono.")
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'phone-input'))
        ).send_keys(data.phone_number)
        time.sleep(9)
        phone_code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'code-input'))
        ).send_keys(phone_code)
        time.sleep(9)

    def test_add_credit_card(self):
        logging.info("Iniciando prueba: agregar tarjeta de crédito.")
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card-number'))
        ).send_keys(data.card_number)
        time.sleep(9)
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card-expiry'))
        ).send_keys(data.card_expiry)
        time.sleep(9)
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cvv-code'))
        ).send_keys(data.card_cvv)
        WebDriverWait(self.driver, 9).until(
            EC.element_to_be_clickable((By.ID, 'comment'))
        ).click()
        time.sleep(9)

    def test_write_driver_message(self):
        logging.info("Iniciando prueba: escribir mensaje para el controlador.")
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.ID, 'comment'))
        ).send_keys("Por favor, traiga agua.")
        time.sleep(9)

    def test_request_extras(self):
        logging.info("Iniciando prueba: pedir manta y pañuelos.")
        self.driver.get(data.urban_routes_url)
        switches = self.driver.find_elements(By.CLASS_NAME, 'switch-input')
        for switch in switches:
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable(switch)
            ).click()
        time.sleep(9)

    def test_request_ice_creams(self):
        logging.info("Iniciando prueba: pedir 2 helados.")
        self.driver.get(data.urban_routes_url)
        for _ in range(2):
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'counter-plus'))
            ).click()
            time.sleep(9)

    def test_search_taxi_modal(self):Testing started at 07:29 p. m. ...
Traceback (most recent call last):
  File "C:/Program Files/JetBrains/nueva7/PyCharm Community Edition 2024.3.4/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py", line 5, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'

Process finished with exit code 1

Empty suite

        logging.info("Iniciando prueba: buscar taxi.")
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 9).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.smart-button-main'))
        ).click()
        time.sleep(9)
        assert WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'order-details'))
        ).is_displayed()

    @classmethod
    def teardown_class(cls):
        logging.info("Cerrando el navegador.")
        time.sleep(9)
        cls.driver.quit()
