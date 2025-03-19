
function limitWords(event) {
  const maxWords = 100; 
  const words = event.target.value.split(/\s+/);
  
  if (words.length > maxWords) {

      event.target.value = words.slice(0, maxWords).join(" ");
  }
}

function preventAdditionalTyping(event) {
  const maxWords = 100;
  const words = event.target.value.split(/\s+/);
  
  if (words.length > maxWords) {
      event.preventDefault(); 
  }
}

// Get Text from the textarea

const txt1 = document.getElementById('input');
const btn1 = document.getElementById('button');
const out1 = document.getElementById('output');

function fun1() {
    out1.innerHTML = txt1.value;
}

btn1.addEventListener('click', fun1);
