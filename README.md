## Описание проекта

# Инструкция по созданию бота и получению его токена
Чтобы создать Telegram-бота и получить токен для его работы, следуйте этим шагам:

1. Создание бота через BotFather
- Откройте приложение Telegram и найдите аккаунт BotFather.
- Отправьте команду /start для начала взаимодействия.
- Отправьте команду /newbot, чтобы создать нового бота.
- Следуйте инструкциям для задания имени и юзернейма вашего бота.
- После успешного создания бота, BotFather пришлет вам токен для доступа к Telegram API (это длинная строка символов).
2. Настройка токена бота
В файле .env в корневой папке проекта добавьте туда токен вашего бота:
   ```bash
   BOT_TOKEN=your_telegram_bot_token
   ```
   
# Инструкция по запуску бота
Следуйте этим шагам для настройки и запуска проекта на вашем локальном компьютере:

1. **Создайте виртуальное окружение в корневой папке проекта**  
В терминале выполните команду:
   ```bash
   python -m venv venv
   ```
3. **Активируйте виртуальное окружение**  
В зависимости от вашей операционной системы, используйте одну из следующих команд:
   - Для Windows:
    ```bash
    venv/scripts/activate
    ```
   - Для macOS/Linux:
    ```bash
   source venv/bin/activate
    ```
5. **Установите все пакеты, указанные в requirements.txt**  
Убедитесь, что виртуальное окружение активировано, и выполните команду:
    ```bash
   pip install -r requirements.txt
7. **Запустите бота**  
В корневой папке проекта выполните команду:
    ```bash
   python bot.py 
    ```
9. **Протестируйте бота**  
В Телеграмма найдите бота @TZ_usdRateBot(https://t.me/TZ_usdRateBot) и нажмите кнопку START.
После этого введите ваше имя, и бот ответит вам сообщением, содержащим ваше имя и актуальный курс доллара США.


