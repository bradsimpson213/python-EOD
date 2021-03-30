// Example #1 Ternary Operator
let isGood = true;
const dragon = isGood ? "Toothless" : "Smaug";
console.log(dragon);


// Example #2 Random Numbers
const dragons = ['Puff', 'Toothless', 'Falkor', 'Draco'];
const randNum = Math.floor(Math.random() * dragons.length);
const dragonPick = dragons[randNum];
console.log(dragonPick);


// Example #3 User Input
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Who is the coolest dragon? ', (answer) => {
  console.log(`You thought ${answer} was the coolest dragon...`);
  rl.close();
});


// Example #4 Importing Files
const fs = require("fs");
let words = [];

fs.readFile("words.txt", "utf8", (err, data) => {
  if (err) {
    console.log(err);
  }
  words = data.split(',');
  console.log(words);
});


// Example #5 Classes
class Book {
  constructor(title, series, author) {
    this.title = title;
    this.series = series;
    this.author = author;
  }
 
  getInformation() {
    return `${this.title} by ${this.author}`;
  }
};


// Example #6 Routes (can't test)
app.get('/item/:id', (req, res) => {
  res.send(`<h1>Item ID: ${req.params.id}</h1>`);
});
