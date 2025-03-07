import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# No modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string."""
    import json
    import time
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

    raise Exception("No se encontró el código de confirmación del teléfono.\n"
                    "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        logging.info(f"Estableciendo la dirección de origen: {from_address}")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        logging.info(f"Estableciendo la dirección de destino: {to_address}")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        logging.info("Obteniendo la dirección de origen.")
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).get_property('value')

    def get_to(self):
        logging.info("Obteniendo la dirección de destino.")
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).get_property('value')

    def set_route(self, address_from, address_to):
        logging.info("Estableciendo la ruta.")
        self.set_from(address_from)
        self.set_to(address_to)

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # No modificar
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        logging.info("Iniciando prueba: establecer ruta.")
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        logging.info("Prueba completada: establecer ruta.")

    @classmethod
    def teardown_class(cls):
        logging.info("Cerrando el navegador.")
        cls.driver.quit()
