# Waze-Police  <img src="https://github.com/dream-eam-belarus/waze-mogilev-telegram/workflows/CI/badge.svg?branch=main"><br>

## works in Mogilev county only.

[🚔 Positions on the map 🚔](https://www.google.com/maps/d/edit?mid=11dV8idADUD93IHeVkneH6D-tjz_a6Q0z&usp=sharing)

Current places:

- Места работы ГАИ в городе
  - ул.Королёва (в сторону моста)                               
  - ДК железнодорожников                                        
  - кафе Дана (Чаусское шоссе)                                  
  - Мясокомбинат (пр-т Пушкинский и ул.Димитрова ДВЕ ТОЧКИ!!!)                                             
  - Телевидение (ул.Первомайская)                               
  - Белтелеком (ул. Болдина)                                    
  - Кулешова                                                    
  - Лифтмаш                                                     
  - Моготекс                                                    
  - Автопарк
  - Шкловское кольцо
  - Лавсановское кладбище 
  - Габрово
  - Драмтеатр
  - БэйкХаус
  - Кольцо Космонавтов
  - Гришина церковь
  - Крупской (съезд в сторону кольца)
  - Обувная фабрика (в сторону казимировки)
  - Музыкальна школа (Шмидта в сторону облгаза)
  - Кирово (в сторону города)
  - Памятник афганцам
  - Зеленый луг
  - Ледовый дворец
  - Университет продовольствия
  - Чаусская трасса (на против заправки в сторону города)
  - Веснянка
  - Дворец гимнастики
  - Пинскдрев (Симонова)
  - VIP Бунгало
  - Электродвигатель
  - Спортландия (Якубовского)
  - ск.Олимпиец (30 лет Победы)
  - ост.Зеленая роща
  - з-д Зенит
  - Стадион Спартак
  - Садко (ул.Лазаренко)
  - Минский рынок
  - ул.Танковая (знак 50)
  - ост.Диагностический центр
  - ул.Яцыно
  - тц.Санта (ул.Габровская)
  - Технопарк
  - Святое озеро
  - пер.Пожарный
  - Виленский рынок
  - ул.Ленинская (КГБ)
  - Зоосад
  - ДК Химволокно
  - ТЦ Арбат ул.Островского
  - ул.Терёхина
  - ул.Крупской (Хит)
  - ул.Тимирязевскаая (Строммашина)
  - ул.Гришина (Школа 25)
  - ул.Чигринова
  - ул.Кутепова
  - к-тр Космос
  - ул.Пысина
  - ул.Льва Сапеги
  - ул. Тишки Гартного
  - Кошкин Дом
  - пер.Т.Карпинской
  - ул.Строителей
  - ул.Челюскинцев
  - ул.Быховская
  - ул.Павлова
  - ул.Вишневецкого (переезд Ямницкий)
  - рынок Любужский
  - Дом Спорта
  - Дворец Пионеров
  - д.Присно
  - д.Малая Боровка
  - д.Большая Боровка
  - Сентябрьский мост
  - ТЦ Ома
  - Стадион Торпедо
  - ул.Актюбинская

---    

- Места работы ГАИ за городом
  - Рудея
  - Стейк и вино
  - Аэропорт
  - д.Буйничи (заправка)
  - д.Фойно
  - д.Тишовка
  - д.Локути
  - д.Романовичи
  - д.Красница
  - г.Шклов
  - д.Межисетки
  - д.Любуж
  - д.Купёлы
  - д.Селец
  - д.Мосток
  - д.Купёлы
  - д.Литовск
  - д.Вишов
  - г.Кировск
  - д.Восход
  - д.Зимница
  - д.Добросневичи
  - д.Новосёлки
  - д.Антоновка
  - д.Княжицы
  - д.Досовичи, д.Дубровка, д.Малинник, д.Перстилы, д.Репище, д.Подбродье
  - д.Воронино
  - д.Следюки
  - д.Годылёво
  - д.Сидоровичи
  - д.Волковичи
  - д.Полетники
  - д.Солтановка
  - д.Быстрик
  - д.Амховая
  - д.Фащевка
  - д.Клин
  - д.Довск
  - д.Мирный
  - г.Чаусы
  - д.Вейно

---

- Места ДТП
  - Мост Якубовского
  - Спуск Ордженикидзе

  
---------------------

# How to deploy


ssh-keygen -t ed25519 -C "mail"
-------------
# Amazon Linux2

sudo amazon-linux-extras install docker -y && sudo service docker start && sudo usermod -a -G docker ec2-user && sudo chkconfig docker on && sudo yum install -y git && sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose

-------------
# OracleCloud Ubuntu 20.04

sudo mkdir waze && sudo apt update && sudo apt install apt-transport-https zip unzip ca-certificates curl gnupg lsb-release -y && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && sudo apt-get update && sudo apt-get install docker-ce docker-ce-cli containerd.io -y && sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && sudo gpasswd -a $USER docker && sudo reboot

-------------
To be continue
