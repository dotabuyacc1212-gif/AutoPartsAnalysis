# Анализ Автозапчастей 🚗🔧

Интерактивное веб-приложение для анализа данных об автомобильных запчастях, созданное с помощью Streamlit.

🌐 **Демо:** [https://autopartsanalysis.streamlit.app/](https://autopartsanalysis.streamlit.app/)

[English version](README.md)

## Возможности

- 📊 Интерактивная визуализация данных о запчастях
- 🔍 Поиск и фильтрация по категориям, производителям и ценам
- 📈 Статистический анализ ценовых трендов
- 💾 Экспорт отфильтрованных результатов в Excel
- 🎨 Современный и адаптивный интерфейс

## Быстрый старт

### Локальная установка

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/auto-parts-analysis.git
cd auto-parts-analysis

# Установите зависимости
pip install -r requirements.txt

# Сгенерируйте тестовые данные
python generate_data.py

# Запустите приложение
streamlit run app.py
```

### Docker

```bash
# Соберите образ
docker build -t auto-parts-analysis .

# Запустите контейнер
docker run -p 8501:8501 auto-parts-analysis
```

Откройте браузер по адресу `http://localhost:8501`

## Структура проекта

```
.
├── app.py                  # Основное Streamlit приложение
├── generate_data.py        # Генератор тестовых данных
├── auto_parts_data.xlsx    # Файл с данными
├── requirements.txt        # Зависимости Python
├── Dockerfile             # Конфигурация Docker
└── .streamlit/
    └── config.toml        # Настройки Streamlit
```

## Технологии

- **Python 3.11+**
- **Streamlit** - Веб-интерфейс
- **Pandas** - Обработка данных
- **Plotly** - Интерактивные графики
- **OpenPyXL** - Работа с Excel файлами

## Лицензия

Лицензия MIT - подробности в файле [LICENSE](LICENSE).

## Участие в разработке

Приветствуются любые предложения! Открывайте issues или отправляйте pull requests.
