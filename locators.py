from selenium.webdriver.common.by import By

# Главная страница
MAIN_PAGE_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет"
CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")  # Кнопка "Конструктор"
LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers

# Форма регистрации
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле "Имя"
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле "Email"
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле "Пароль"
REGISTER_SUBMIT = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться" для подтверждения регистрации
PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")  # Ошибка пароля и наличие класса у поля пароль (красная обводка)
LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка "Войти"

# Форма входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле Email входа
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле Пароля входа
LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # Ссылка "Зарегистрироваться"
RECOVERY_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль"

# Личный кабинет
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка "Выход"

# Конструктор
BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  # Раздел "Булки"
SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Раздел "Соусы"
FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Раздел "Начинки"
ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Класс "Активный раздел"