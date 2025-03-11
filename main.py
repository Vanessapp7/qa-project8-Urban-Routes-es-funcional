import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.INFO)

# No modificar
def retrieve_phone_code(driver) -> str:
    import json
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [
                log["message"] for log in driver.get_log('performance')
                if log.get("message") and 'api/v1/number?number' in log.get("message")
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                logging.info(f"Código de confirmación obtenido: {code}")
        except WebDriverException as e:
            logging.warning(f"Error al obtener el código: {e}")
            WebDriverWait(driver, 5).until(lambda d: True)
        if code:
            return code
    raise Exception("No se encontró el código de confirmación del teléfono.")

class UrbanRoutesPage:
    # Localizadores actualizados y nuevos añadidos
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    comfort_tariff_button = (By.CLASS_NAME, 'comfort-tariff')
    phone_input = (By.CLASS_NAME, 'phone-input')
    code_input = (By.CLASS_NAME, 'code-input')
    phone_verified = (By.CLASS_NAME, 'phone-verified')
    card_number = (By.CLASS_NAME, 'card-number')
    card_expiry = (By.CLASS_NAME, 'card-expiry')
    card_cvv = (By.CLASS_NAME, 'cvv-code')
    credit_card_added = (By.CLASS_NAME, 'credit-card-added')
    message_to_driver_field = (By.ID, "comment")
    added_card_field = (By.XPATH, "//div[@class='pp-tittle' and text()='Tarjeta']")
    pay_method_close_button = (By.XPATH, "//div[@class='payment-picker open']//button[@class]")
    blanket_and_handkerchief_switch = (By.CLASS_NAME, 'switch')
    blanket_and_handkerchief_input = (By.CLASS_NAME, 'switch-input')
    ice_cream_counter_plus = (By.CLASS_NAME, 'counter-plus')
    request_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    countdown_modal = (By.CLASS_NAME, "order-details")
    driver_name = (By.XPATH, '//div[@class="order-btn-group"]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        logging.info(f"Estableciendo la dirección de origen: {from_address}")
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        logging.info(f"Estableciendo la dirección de destino: {to_address}")
        WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        logging.info("Obteniendo la dirección de origen.")
        return WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located(self.from_field)
        ).get_property('value')

    def get_to(self):
        logging.info("Obteniendo la dirección de destino.")
        return WebDriverWait(self.driver, 9).until(
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
        assert routes_page.get_from() == address_from, "El origen no coincide."
        assert routes_page.get_to() == address_to, "El destino no coincide."

    def test_select_comfort_tariff(self):
        logging.info("Iniciando prueba: seleccionar tarifa Comfort.")
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 9).until(
            EC.element_to_be_clickable(UrbanRoutesPage.comfort_tariff_button)
        ).click()
        selected_tariff = WebDriverWait(self.driver, 9).until(
            EC.presence_of_element_located((By.CLASS_NAME, "selected-tariff"))
        )
        assert selected_tariff.is_displayed(), "La tarifa Comfort no fue seleccionada correctamente."

    @classmethod
    def teardown_class(cls):
        logging.info("Cerrando el navegador.")
        cls.driver.quit()
