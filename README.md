<h1 align="center">ETL Pipeline - Пример ETL-пайплайна для обработки данных</h1>

<p align="center">
  <em>Базовый ETL-пайплайн для извлечения, преобразования и загрузки данных в PostgreSQL.</em>
</p>

## О проекте

<p>
  Этот проект представляет собой базовый ETL-пайплайн, который извлекает данные из публичного API (**Random User API**), преобразует их с помощью библиотеки **Pandas** и загружает в базу данных **PostgreSQL**.  
  Проект включает использование **SQLAlchemy** для подключения к базе данных и **logging** для логирования всех шагов.
</p>

## Содержание

<ul>
  <li><a href="#функциональные-возможности">Функциональные возможности</a></li>
  <li><a href="#установка">Установка</a></li>
  <li><a href="#использование">Использование</a></li>
  <li><a href="#контакты">Контакты</a></li>
</ul>

## Функциональные возможности

<ul>
  <li>Извлечение данных из публичного API.</li>
  <li>Преобразование данных с использованием библиотеки Pandas.</li>
  <li>Загрузка данных в базу данных PostgreSQL.</li>
  <li>Логирование выполнения шагов ETL-пайплайна.</li>
</ul>

## Установка

<ol>
  <li>Клонируйте репозиторий:
    <pre><code>git clone https://github.com/BOCXO2/etl-pipeline.git</code></pre>
  </li>
  <li>Перейдите в директорию проекта:
    <pre><code>cd etl-pipeline</code></pre>
  </li>
  <li>Создайте и активируйте виртуальное окружение:
    <pre><code>python -m venv env
source env/bin/activate  # Для Windows: env\Scripts\activate</code></pre>
  </li>
  <li>Установите необходимые зависимости:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Создайте файл <code>config.py</code> и добавьте данные для подключения к вашей базе данных PostgreSQL:
    <pre><code>DB_CONFIG = {
  "user": "your_user",
  "password": "your_password",
  "host": "localhost",
  "port": "5432",
  "database": "etl_db"
}</code></pre>
  </li>
  <li>Запустите пайплайн:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

## Использование

<ol>
  <li>Запустите проект с помощью команды <code>python main.py</code>.</li>
  <li>Пайплайн автоматически извлечет, преобразует и загрузит данные в вашу базу данных PostgreSQL.</li>
  <li>Логи выполнения сохраняются в файл <code>etl.log</code>.</li>
</ol>

## Контакты

<p>
  Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с автором проекта через <a href="https://github.com/BOCXO2">профиль GitHub</a>.
</p>

