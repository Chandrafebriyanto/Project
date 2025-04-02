let x ="pizza";
let y ="pizza";
let z ="pizza";

x = Number(x); // untuk mengubah data menjadi nilai integar/angka
y = String(y); // untuk mengubah data menjadi nilai string/teks
z = Boolean(z); // untuk mengubah data menjadi nilai boolean (true/false)

console.log(x, typeof x);
console.log(y, typeof y);
console.log(z, typeof z);

//penjelasan
/* 
default dari nilai variabel adalah string
1. jika nilai awal dari variabel adalah string kemudian diubah menjadi integer (number) maka hasil yang keluar adalah NaN atau tidak bisa
2. jika nilai awal dari variabel adalah string kemudian diubah menjadi boolean makah hasil yang keluar adalah "True"
*/
