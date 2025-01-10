// let num1 = 180;
// let num2 = 100;
// let num3 = 120;
//
// console.log(num2,  num3, num1)
//
//
// const s = 'Светлана'
// console.log(s)


// let year = 96
// console.log(year)
// console.log('Прошел год')
// year = 97
// console.log(year)


// let source
// let destination
// source = 'sigma'
// destination = source
// source = 'delta'
// console.log(source)
// console.log(destination)



//
// const prod = prompt();
// console.log(prod);


//
// const num1 = Number(prompt());
// const num2 = Number(prompt());
// console.log(num1, num2);


// const word1 = prompt();
// const word2 = prompt();
// console.log(word2);
// console.log(word1);



//
// const num1 = Number(prompt());
// const num2 = Number(prompt());
// const num3 = Number(prompt());
// console.log(num1 * num2 * num3);



// const num1 = Number(prompt());
// let allPrice = num1 * 110
// console.log('Стоимость партии чипсов:', allPrice, 'рублей');
//
//
// const num1 = Number(prompt());
//
// console.log(num1 % 4);



// const num1 = Number(prompt());
// const num2 = Number(prompt());
// console.log((num1 + num2) / 2);


// console.log( '12' < 5 );



// const num1 = Number(prompt());
// const num2 = Number(prompt());
// console.log(num1 !== num2);


// const num1 = Number(prompt());
// const num2 = Number(prompt());
// const num3 = Number(prompt());
// console.log(num1 + num2 === num2 + num3);



// const num1 = Number(prompt());
// const num2 = Number(prompt());
// console.log(num1 < num2);


// const num1 = Number(prompt());
// if (num1 % 2 == 0 && num1 > 0) {
//     console.log('Четное и положительное')
// }

// const num1 = prompt();
// if (num1.length >= 3) {
//     console.log('Трехзначное')
// }


// const num1 = Number(prompt());
//
// if (num1  >= 1000) {
//     console.log(num1 * 0.9)
// }
// console.log('Спасибо за покупку')


// const num1 = Number(prompt());
//
// if (num1  % 2) {
//     console.log('Число нечетное')
// } else {console.log('Число четное')}
//
//
// if (!num1) {
//     console.log('Не положительное и не отрицательное')
// } else if (num1 > 0) {console.log('Положительное')
// } else {console.log('Отрицательное')}

// const num1 = Number(prompt());
// if (num1 >= 84) {
//     console.log('Отлично')
// } else if (num1 >= 64) {console.log('Хорошо')
// } else {console.log('Учись')}


// const num1 = Number(prompt());
// if ( 0 <= num1 && num1 <= 11) {
//     console.log('Доброе утро')
// } else if (12 <= num1 && num1 <= 17) {console.log('Добрый день')
// } else {console.log('Добрый вечер')}
//
//
//
// const num1 = Number(prompt());
// if ( 1 <= num1 && num1 <= 3) {
//     console.log('Плохое')
// } else if (4 <= num1 && num1 <= 7) {console.log('Нормальное')
// } else if (8 <= num1 && num1 <= 10) {console.log('Хорошее')
// } else {console.log('Число вне диапазона')}


// Если длина меньше или равно 3.8 м и объем двигателя меньше или равно 1.2 л, результат - "Класс A".
// Если длина меньше или равно 4 м и объем двигателя меньше или равно 1.6 л, результат - "Класс B".
// Если длина меньше или равно 4.5 м и объем двигателя от 1.6 до 2 л включительно, результат - "Класс C".
// В противном случае, результат - "Выберите автомобиль другого класса".

const lenAuto = Number(prompt());
const motor = Number(prompt());
if ( 3.8 >= lenAuto && motor <= 1.2) {
    console.log('Класс A')
} else if (4 >= lenAuto && motor <= 1.6) {console.log('Класс B')
} else if (4.5 >= lenAuto && (motor <= 2 && motor >= 1.6)) {console.log('Класс C')
} else {console.log('Выберите автомобиль другого класса')}
