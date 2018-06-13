# vk_tests
Тест скорости bots longpool и callback API. +Тест скорости Flask и Bottle в рамках ботов для ВК

4 файла:
1. callback_flask - тест callback API с фреймфорком Flask
2. callback_bottle - тест callback API с фреймворком Bottle
3. longpool - тест longpool'а
4. flask_req - привязка группы ВК к этому IP

Спойлер: callback быстрее longpool'а. Результат зависит от скорости соединения до ВК:

Результаты, секунды (два числа, один - с моего ПК, другой - с сервера):
callback_Bottle - 0.025, 0.0048
callback_Flask - 0.027, 0.0098
longpool - 0.075, 0.0748
