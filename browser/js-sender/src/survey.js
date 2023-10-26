// (function () {
//   // Helper function to click a random element with a given class
//   function clickRandomClickableCellElement() {
//     const elements = document.querySelectorAll('[class*="input"]');
//     if (elements.length > 0) {
//       const randomIndex = Math.floor(Math.random() * elements.length);
//       elements[randomIndex].click();
//     }
//   }

//   // Function to simulate random clicks
//   function simulateRandomClicks() {
//     setInterval(function () {
//       const randomNumber = Math.random();
//       if (randomNumber < 0.8) {
//         console.log("clicking clickable cell");
//         // Click a random element with "clickableCell" in the class
//         clickRandomClickableCellElement();
//       } else {
//         // Click the second element
//         document.getElementById("btn_continue").click();
//       }
//     }, 1000); // Adjust the interval (in milliseconds) as needed
//   }
//   simulateRandomClicks();
// })();

// Get all the <tr> elements with the class "ChoiceRow"
const choiceRows = document.querySelectorAll("tr.ChoiceRow");

choiceRows.forEach((row) => {
  // Get all the <td> elements within the current <tr>
  const tdElements = row.querySelectorAll("td");

  // Generate a random index to select a random <td> element
  const randomIndex = Math.floor(Math.random() * tdElements.length);

  // Click the randomly selected <td> element
  tdElements[randomIndex].click();
});
