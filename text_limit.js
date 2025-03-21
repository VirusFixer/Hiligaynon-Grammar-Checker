function preventAdditionalTyping(event) {
  const maxWords = 100;
  const words = event.target.value.split(/\s+/);

  if (words.length >= maxWords) {
      event.preventDefault(); 
  }
}