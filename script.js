function limitWords(event) {
    const input = event.target.value;
    const words = input.trim().split(/\s+/); 
    if (words.length > 20) {
      
      event.target.value = words.slice(0, 20).join(' ');
    }
  }

  function preventAdditionalTyping(event) {
    const input = event.target.value;
    const words = input.trim().split(/\s+/);
    if (words.length >= 20 && event.key !== "Backspace" && event.key !== "Delete") {
      event.preventDefault(); 
    }
  }