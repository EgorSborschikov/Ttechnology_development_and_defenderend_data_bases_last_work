# Описание предметной области интернет-магазина

## Введение

Структура информационной системы нужно разработать с учетом того, чтобы проектируемый интернет-магазин мог успешно выполнять следующие функции:

- Хранение данных пользователей (авторизационных данных и данных "Личного кабинета");
- Двух (или более) уровневую каталогизацию товаров;
- Просмотр товаров по заданным критериям;
- Просмотр историю заказов, сделанных пользователями;
- Отбор товаров в корзину;
- Формирование заказа из нескольких товаров.

Необходимо учесть, что каждый товар имеет уникальный номер, полное наименование и характеристики товара (специфичные для той области, для которой создается интернет-магазин).

## Обязательные характеристики товара

- Основное фото;
- Дополнительные фото (3-6);
- Название;
- Артикул;
- Цена;
- Количество на складе;
- Текстовое описание.

## Учет скидок и акционных предложений

Структура информационной системы должна предусматривать учет скидок на товары, акционных предложений и других подобного рода мероприятий:

- Для товаров, которые участвуют в распродаже, указывается скидка;
- Для товаров, которые являются "Хитами продаж", устанавливается дополнительный параметр;
- Для товаров, которые только поступили в продажу ("Новинки"), устанавливается дополнительный параметр;
- Для товаров, которые участвуют в "Акции", присваивается номер акции (варианты акций должны быть предусмотрены в структуре информационной системы).

## Способы оплаты и доставки

При формировании заказа покупателю предлагается использовать различные способы оплаты и доставки: on-line заказ, оформление доставки на дом. Для этого в информационной системе должны быть предусмотрены различные способы оплаты (кредитные карты, электронные деньги, оплату наличными курьеру, оплату наличными при получении на почте) и различные способы доставки (самовывоз, доставка).

## Модели данных

Модели данных предоставлены в ER-диаграмме базы данных [docs/ER-diagrams.png]