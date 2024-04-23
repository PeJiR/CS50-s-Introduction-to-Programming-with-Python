const userInput = document.getElementById('user-input');
const resultsDiv = document.getElementById('results-div');
const checkBtn = document.getElementById('check-btn');
const clearBtn = document.getElementById('clear-btn');

const checkValidNumber = input => {
  if (input === "") {
    alert("Please provide a phone number");
    return;
  }
  // Regular expression to match valid US phone number formats
const regex = /^(1\s?)?(\(\d{3}\)|\d{3})[-\s]?\d{3}[-\s]?\d{4}$/;
const phoneRegex = new RegExp(regex);

   
const pTag = document.createElement('p');
pTag.className = "results-text";
phoneRegex.test(input)
  ? (pTag.style.color = 'var(--green')
  : (pTag.style.color = '4d3800');
pTag.appendChild(
  document.createTextNode(
    `${phoneRegex.test(input) ? 'Valid' : 'Invalid'} US number: ${input} `
  )
);
resultsDiv.appendChild(pTag);
};


checkBtn.addEventListener('click', () => {
  checkValidNumber(userInput.value);
  userInput.value = '';
});

userInput.addEventListener('keydown', e => {
  if (e.ket === "Enter") {
    checkValidNumber(user.input.value);
    userInput.value = '';
  }
});

clearBtn.addEventListener('click', () => {
  resultsDiv.textContent = '';
})

// Test the function with the input "555-555-5555"
console.log(telephoneCheck("555-555-5555")); // Output: true